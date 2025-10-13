import { useEffect, useRef, useState } from 'react';

interface Node {
  x: number;
  y: number;
  vx: number;
  vy: number;
  radius: number;
  connections: number[];
  pulsePhase: number;
  pulseSpeed: number;
  depth: number; // For layering effect
  targetVx: number; // For smoother movement
  targetVy: number;
  alphaMultiplier: number; // For fading in exclusion zones
}

interface Particle {
  x: number;
  y: number;
  vx: number;
  vy: number;
  life: number;
  maxLife: number;
  alpha: number;
  depth: number; // For layering
  size: number; // Variable size for depth perception
}

interface DataPulse {
  fromNode: number;
  toNode: number;
  progress: number;
  speed: number;
  color: string;
  trail: { x: number; y: number; alpha: number }[]; // Trail effect
}

export interface ExclusionZone {
  x: number;
  y: number;
  width: number;
  height: number;
  strength?: number; // Repulsion strength multiplier (default 1)
}

interface NeuralBackgroundProps {
  nodeCount?: number;
  particleCount?: number;
  connectionDistance?: number;
  interactive?: boolean;
  intensity?: 'low' | 'medium' | 'high';
  className?: string;
  exclusionZones?: ExclusionZone[]; // Zones to keep nodes away from
  debugZones?: boolean; // Show exclusion zones for debugging
}

/**
 * Optimized Neural Network Background Component
 * 
 * Performance optimizations applied:
 * - Squared distance calculations to avoid expensive sqrt operations
 * - Cached constant values (connectionDistSq, invConnectionDistance, etc.)
 * - Early exit conditions for invisible elements
 * - Batched particle rendering by brightness to reduce fillStyle changes
 * - Pre-allocated arrays and reused references
 * - Bit shift operations for faster Math.floor
 * - Debounced exclusion zone calculations
 * - Node sorting only every 60 frames (depth doesn't change)
 * - Hoisted calculations out of loops
 * - Canvas context optimized with desynchronized hint
 * - Reduced object allocations and redundant calculations
 */
const NeuralBackground = ({ 
  nodeCount = 40,
  particleCount = 600,
  connectionDistance = 200,
  interactive = true,
  intensity = 'medium',
  className = '',
  exclusionZones = [],
  debugZones = false
}: NeuralBackgroundProps) => {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const animationRef = useRef<number | undefined>(undefined);
  const nodesRef = useRef<Node[]>([]);
  const particlesRef = useRef<Particle[]>([]);
  const pulsesRef = useRef<DataPulse[]>([]);
  const mouseRef = useRef({ x: 0, y: 0, isActive: false });
  const [prefersReducedMotion, setPrefersReducedMotion] = useState(false);
  const sortedNodesRef = useRef<Node[]>([]);
  const frameCountRef = useRef(0);
  const connectionDistSqRef = useRef(connectionDistance * connectionDistance);

  // Update cached connection distance when it changes
  useEffect(() => {
    connectionDistSqRef.current = connectionDistance * connectionDistance;
  }, [connectionDistance]);

  // Check for reduced motion preference
  useEffect(() => {
    const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
    setPrefersReducedMotion(mediaQuery.matches);
    
    const handler = (e: MediaQueryListEvent) => setPrefersReducedMotion(e.matches);
    mediaQuery.addEventListener('change', handler);
    return () => mediaQuery.removeEventListener('change', handler);
  }, []);

  // Adjust parameters based on intensity
  const getIntensityParams = () => {
    switch (intensity) {
      case 'low':
        return { nodeSpeed: 0.12, pulseFrequency: 0.0015, particleAlpha: 0.18 };
      case 'high':
        return { nodeSpeed: 0.35, pulseFrequency: 0.007, particleAlpha: 0.38 };
      default:
        return { nodeSpeed: 0.22, pulseFrequency: 0.004, particleAlpha: 0.28 };
    }
  };

  const params = getIntensityParams();

  // Initialize nodes
  const initNodes = (width: number, height: number) => {
    const nodes: Node[] = [];
    for (let i = 0; i < nodeCount; i++) {
      const depth = Math.random(); // 0 to 1, closer = larger
      const speedMultiplier = 0.5 + depth * 0.5; // Closer nodes move slower
      const targetVx = (Math.random() - 0.5) * params.nodeSpeed * speedMultiplier;
      const targetVy = (Math.random() - 0.5) * params.nodeSpeed * speedMultiplier;
      
      nodes.push({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: targetVx,
        vy: targetVy,
        targetVx,
        targetVy,
        radius: Math.random() * 1.5 + 1 + depth * 1.5, // Depth affects size
        connections: [],
        pulsePhase: Math.random() * Math.PI * 2,
        pulseSpeed: Math.random() * 0.02 + 0.01,
        depth,
        alphaMultiplier: 1
      });
    }
    return nodes;
  };

  // Initialize particles
  const initParticles = (width: number, height: number) => {
    const particles: Particle[] = [];
    for (let i = 0; i < particleCount; i++) {
      particles.push(createParticle(width, height));
    }
    return particles;
  };

  const createParticle = (width: number, height: number): Particle => {
    const maxLife = Math.random() * 100 + 100;
    const depth = Math.random();
    // Add subtle flow direction (slightly upward and to the right)
    const flowVx = 0.05;
    const flowVy = -0.03;
    
    return {
      x: Math.random() * width,
      y: Math.random() * height,
      vx: (Math.random() - 0.5) * 0.3 + flowVx * depth,
      vy: (Math.random() - 0.5) * 0.3 + flowVy * depth,
      life: maxLife,
      maxLife,
      alpha: Math.random() * 0.3 + 0.1,
      depth,
      size: 0.5 + depth * 1.5 // Closer particles are larger
    };
  };

  // Calculate fade effect from exclusion zones for nodes (optimized)
  const calculateZoneRepulsion = (node: Node, zones: ExclusionZone[]) => {
    if (zones.length === 0) return { repulsionX: 0, repulsionY: 0, alphaMultiplier: 1 }; // Early exit
    
    let repulsionX = 0;
    let repulsionY = 0;
    let alphaMultiplier = 1;
    
    for (let i = 0; i < zones.length; i++) {
      const zone = zones[i];
      const strength = zone.strength ?? 1;
      
      // Pre-calculate zone bounds
      const zoneRight = zone.x + zone.width;
      const zoneBottom = zone.y + zone.height;
      
      // Calculate closest point on rectangle to node
      const closestX = Math.max(zone.x, Math.min(node.x, zoneRight));
      const closestY = Math.max(zone.y, Math.min(node.y, zoneBottom));
      
      const dx = node.x - closestX;
      const dy = node.y - closestY;
      const distSq = dx * dx + dy * dy;
      
      // Check if node is inside zone
      const isInside = node.x >= zone.x && node.x <= zoneRight &&
                       node.y >= zone.y && node.y <= zoneBottom;
      
      if (isInside) {
        // Make nodes completely invisible inside zones
        alphaMultiplier = 0;
        
        // Strong repulsion to push nodes out - avoid sqrt when dist is 0
        if (distSq > 0) {
          const invDist = 1 / Math.sqrt(distSq);
          repulsionX += dx * invDist * 0.2 * strength;
          repulsionY += dy * invDist * 0.2 * strength;
        }
      } else if (distSq < 2500) { // 50*50 = 2500
        // Fade as approaching zone (soft feathered edge) - only sqrt when needed
        const dist = Math.sqrt(distSq);
        const fadeEdge = (50 - dist) * 0.02; // Multiply by 1/50 instead of dividing
        alphaMultiplier = Math.min(alphaMultiplier, 1 - fadeEdge * strength);
      }
    }
    
    return { repulsionX, repulsionY, alphaMultiplier };
  };

  // Calculate fade effect from exclusion zones for particles (optimized with early exits)
  const calculateParticleZoneFade = (x: number, y: number, zones: ExclusionZone[]) => {
    if (zones.length === 0) return 1; // Early exit if no zones
    
    let alphaMultiplier = 1;
    
    for (let i = 0; i < zones.length; i++) {
      const zone = zones[i];
      const strength = zone.strength ?? 1;
      
      // Quick bounds check first
      const zoneRight = zone.x + zone.width;
      const zoneBottom = zone.y + zone.height;
      
      // Check if particle is inside zone
      if (x >= zone.x && x <= zoneRight && y >= zone.y && y <= zoneBottom) {
        return 0; // Early exit optimization
      }
      
      // Calculate distance to zone (optimized with early exit on distance check)
      const closestX = Math.max(zone.x, Math.min(x, zoneRight));
      const closestY = Math.max(zone.y, Math.min(y, zoneBottom));
      const dx = x - closestX;
      const dy = y - closestY;
      const distSq = dx * dx + dy * dy;
      
      if (distSq < 2500) { // 50*50 = 2500
        // Only compute sqrt when needed
        const dist = Math.sqrt(distSq);
        const fadeEdge = (50 - dist) * 0.02; // Multiply by 1/50 instead of dividing
        alphaMultiplier = Math.min(alphaMultiplier, 1 - fadeEdge * strength);
      }
    }
    
    return alphaMultiplier;
  };

  // Create data pulse
  const createDataPulse = (nodes: Node[]) => {
    if (Math.random() > params.pulseFrequency) return;
    
    const fromNode = Math.floor(Math.random() * nodes.length);
    const connections = nodes[fromNode].connections;
    if (connections.length === 0) return;
    
    const toNode = connections[Math.floor(Math.random() * connections.length)];
    
    const colors = [
      'rgba(14, 116, 144, 0.8)',  // primary (cyan-blue)
      'rgba(139, 92, 246, 0.8)',  // secondary (purple)
      'rgba(240, 109, 89, 0.8)'   // accent (coral)
    ];
    
    pulsesRef.current.push({
      fromNode,
      toNode,
      progress: 0,
      speed: Math.random() * 0.015 + 0.01,
      color: colors[Math.floor(Math.random() * colors.length)],
      trail: []
    });
  };

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d', { 
      alpha: true,
      desynchronized: true, // Hint for better performance
      willReadFrequently: false // We're not reading pixels
    });
    if (!ctx) return;

    // Set canvas size
    const resize = () => {
      const dpr = window.devicePixelRatio || 1;
      // Get parent dimensions or fallback to window
      const parent = canvas.parentElement;
      const width = parent ? parent.offsetWidth : window.innerWidth;
      const height = parent ? parent.offsetHeight : window.innerHeight;
      
      // Only proceed if we have valid dimensions
      if (width === 0 || height === 0) return;
      
      canvas.width = width * dpr;
      canvas.height = height * dpr;
      canvas.style.width = `${width}px`;
      canvas.style.height = `${height}px`;
      ctx.scale(dpr, dpr);
      
      // Reinitialize nodes if dimensions changed significantly or first time
      const shouldReinit = nodesRef.current.length === 0 || 
        (nodesRef.current.length > 0 && 
         (Math.abs(nodesRef.current[0].x) > width || Math.abs(nodesRef.current[0].y) > height));
      
      if (shouldReinit) {
        nodesRef.current = initNodes(width, height);
        particlesRef.current = initParticles(width, height);
      }
    };

    // Initial resize with small delay to ensure parent has dimensions
    setTimeout(resize, 0);
    window.addEventListener('resize', resize);

    // Mouse interaction
    const handleMouseMove = (e: MouseEvent) => {
      if (!interactive) return;
      const rect = canvas.getBoundingClientRect();
      mouseRef.current = {
        x: e.clientX - rect.left,
        y: e.clientY - rect.top,
        isActive: true
      };
    };

    const handleMouseLeave = () => {
      mouseRef.current.isActive = false;
    };

    if (interactive) {
      canvas.addEventListener('mousemove', handleMouseMove);
      canvas.addEventListener('mouseleave', handleMouseLeave);
    }

    // Animation loop
    const animate = () => {
      const parent = canvas.parentElement;
      const width = parent ? parent.offsetWidth : window.innerWidth;
      const height = parent ? parent.offsetHeight : window.innerHeight;

      // Skip if no valid dimensions yet
      if (width === 0 || height === 0) {
        animationRef.current = requestAnimationFrame(animate);
        return;
      }

      if (prefersReducedMotion) {
        // Static render for reduced motion
        drawStatic(ctx, width, height);
        return;
      }

      // Clear canvas with subtle trail effect for smoother motion blur
      ctx.fillStyle = 'rgba(0, 0, 0, 0.08)';
      ctx.fillRect(0, 0, width, height);

      const nodes = nodesRef.current;
      const particles = particlesRef.current;
      const pulses = pulsesRef.current;

      // Initialize if needed
      if (nodes.length === 0) {
        nodesRef.current = initNodes(width, height);
        particlesRef.current = initParticles(width, height);
        animationRef.current = requestAnimationFrame(animate);
        return;
      }

      // Update and draw particles (background layer)
      // Batch particles by brightness for fewer fillStyle changes
      const particleBatches: { [key: string]: { x: number; y: number; size: number; alpha: number }[] } = {};
      
      // Pre-calculate batch for reuse
      ctx.save();
      const hasZones = exclusionZones.length > 0;
      
      for (let i = particles.length - 1; i >= 0; i--) {
        const p = particles[i];
        
        // Update position
        p.x += p.vx;
        p.y += p.vy;
        p.life--;

        // Wrap around edges (optimized with fewer conditionals)
        if (p.x < 0) p.x = width;
        else if (p.x > width) p.x = 0;
        if (p.y < 0) p.y = height;
        else if (p.y > height) p.y = 0;

        // Reset dead particles
        if (p.life <= 0) {
          particles[i] = createParticle(width, height);
          continue;
        }

        // Calculate alpha before zone fade for early exit
        const lifeRatio = p.life / p.maxLife;
        const baseAlpha = p.alpha * lifeRatio * params.particleAlpha * (0.5 + p.depth * 0.5);
        
        // Early skip if base alpha is too low
        if (baseAlpha <= 0.01) continue;

        // Apply exclusion zone fade to particles (only if zones exist)
        let alpha = baseAlpha;
        if (hasZones) {
          const zoneFade = calculateParticleZoneFade(p.x, p.y, exclusionZones);
          if (zoneFade === 0) continue; // Skip if completely faded by zone
          alpha *= zoneFade;
          if (alpha <= 0.01) continue; // Skip drawing if completely faded
        }

        // Batch by brightness for performance - use bit shift for faster floor
        const brightness = 99 + ((p.depth * 80) | 0);
        const key = brightness.toString();
        if (!particleBatches[key]) particleBatches[key] = [];
        particleBatches[key].push({ x: p.x, y: p.y, size: p.size, alpha });
      }

      // Draw batched particles (reduced fillStyle changes with globalAlpha batching)
      const PI2 = Math.PI * 2;
      ctx.save();
      
      for (const [brightness, batch] of Object.entries(particleBatches)) {
        const b = parseInt(brightness);
        const batchLength = batch.length;
        const colorStr = `rgba(${b}, ${b + 80}, 237, 1)`;
        
        // Group by alpha buckets for fewer state changes (round to nearest 0.1)
        const alphaBuckets: { [key: string]: typeof batch } = {};
        for (let j = 0; j < batchLength; j++) {
          const p = batch[j];
          const alphaKey = ((p.alpha * 10 | 0) / 10).toFixed(1);
          if (!alphaBuckets[alphaKey]) alphaBuckets[alphaKey] = [];
          alphaBuckets[alphaKey].push(p);
        }
        
        // Draw each alpha bucket with single globalAlpha setting
        for (const [alphaStr, alphaBatch] of Object.entries(alphaBuckets)) {
          ctx.globalAlpha = parseFloat(alphaStr);
          ctx.fillStyle = colorStr;
          
          // Draw all particles in this alpha bucket
          for (let j = 0; j < alphaBatch.length; j++) {
            const p = alphaBatch[j];
            if (p.size > 1) {
              ctx.beginPath();
              ctx.arc(p.x, p.y, p.size * 0.5, 0, PI2);
              ctx.fill();
            } else {
              ctx.fillRect(p.x, p.y, p.size, p.size);
            }
          }
        }
      }
      
      ctx.globalAlpha = 1;
      ctx.restore();

      // Update nodes (optimized with early exits and cached values)
      const edgeMargin = 20;
      const widthMinusMargin = width - edgeMargin;
      const heightMinusMargin = height - edgeMargin;
      const mouseActive = interactive && mouseRef.current.isActive;
      const mouseX = mouseRef.current.x;
      const mouseY = mouseRef.current.y;
      
      for (let i = 0; i < nodes.length; i++) {
        const node = nodes[i];
        
        // Apply exclusion zone repulsion (only if zones exist)
        if (hasZones) {
          const zoneResult = calculateZoneRepulsion(node, exclusionZones);
          node.targetVx += zoneResult.repulsionX;
          node.targetVy += zoneResult.repulsionY;
          node.alphaMultiplier = zoneResult.alphaMultiplier;
        } else {
          node.alphaMultiplier = 1;
        }
        
        // Smooth velocity interpolation for organic movement (cached constant)
        const velocityLerp = 0.05;
        node.vx += (node.targetVx - node.vx) * velocityLerp;
        node.vy += (node.targetVy - node.vy) * velocityLerp;
        
        // Update position
        node.x += node.vx;
        node.y += node.vy;

        // Smooth edge bouncing with slight randomization (combined conditionals)
        if (node.x < edgeMargin || node.x > widthMinusMargin) {
          node.targetVx *= -0.95;
          node.targetVx += (Math.random() - 0.5) * 0.05;
          node.x = Math.max(edgeMargin, Math.min(widthMinusMargin, node.x));
        }
        if (node.y < edgeMargin || node.y > heightMinusMargin) {
          node.targetVy *= -0.95;
          node.targetVy += (Math.random() - 0.5) * 0.05;
          node.y = Math.max(edgeMargin, Math.min(heightMinusMargin, node.y));
        }

        // Enhanced mouse interaction with smoother force application
        if (mouseActive) {
          const dx = mouseX - node.x;
          const dy = mouseY - node.y;
          const distSq = dx * dx + dy * dy;
          
          if (distSq < 40000) { // 200*200 = 40000
            // Attraction force that falls off smoothly (optimized calculations)
            const dist = Math.sqrt(distSq);
            const force = (200 - dist) * 0.005; // Multiply by 1/200 instead of dividing
            const smoothForce = force * force * 0.15 * (1 + node.depth * 0.5);
            const invDist = 1 / dist;
            node.targetVx += dx * invDist * smoothForce;
            node.targetVy += dy * invDist * smoothForce;
            
            // Limit velocity (optimized)
            const velSq = node.targetVx * node.targetVx + node.targetVy * node.targetVy;
            if (velSq > 4) { // 2*2 = 4
              const invVel = 2 / Math.sqrt(velSq);
              node.targetVx *= invVel;
              node.targetVy *= invVel;
            }
          }
        }

        // Slight velocity damping for organic feel
        node.targetVx *= 0.998;
        node.targetVy *= 0.998;

        // Update pulse with subtle variation
        node.pulsePhase += node.pulseSpeed;
      }

      // Find connections - optimized with distance squared and cached values
      const connectionDistSq = connectionDistSqRef.current;
      const invConnectionDistance = 1 / connectionDistance;
      const nodesLength = nodes.length;
      
      // Pre-allocate connection arrays
      for (let i = 0; i < nodesLength; i++) {
        nodes[i].connections = [];
      }
      
      // Find and draw connections in one pass to reduce iterations
      for (let i = 0; i < nodesLength; i++) {
        const nodeI = nodes[i];
        const nodeIx = nodeI.x;
        const nodeIy = nodeI.y;
        const nodeIDepth = nodeI.depth;
        const nodeIAlpha = nodeI.alphaMultiplier;
        
        for (let j = i + 1; j < nodesLength; j++) {
          const nodeJ = nodes[j];
          const dx = nodeIx - nodeJ.x;
          const dy = nodeIy - nodeJ.y;
          const distSq = dx * dx + dy * dy;
          
          if (distSq < connectionDistSq) {
            nodeI.connections.push(j);
            nodeJ.connections.push(i);
            
            // Calculate dist only when needed for drawing (optimized)
            const dist = Math.sqrt(distSq);
            const distRatio = 1 - dist * invConnectionDistance;
            const avgDepth = (nodeIDepth + nodeJ.depth) * 0.5;
            const avgAlpha = (nodeIAlpha + nodeJ.alphaMultiplier) * 0.5;
            const alpha = distRatio * 0.12 * (0.6 + avgDepth * 0.4) * avgAlpha;
            
            // Skip drawing if completely transparent
            if (alpha <= 0.01) continue;
            
            const lineWidth = 0.3 + distRatio * 0.8 * avgDepth;
            
            // Create gradient along the line for depth
            const gradient = ctx.createLinearGradient(
              nodeIx, nodeIy,
              nodeJ.x, nodeJ.y
            );
            const alpha1 = alpha * (0.7 + nodeIDepth * 0.3);
            const alpha2 = alpha * (0.7 + nodeJ.depth * 0.3);
            gradient.addColorStop(0, `rgba(99, 179, 237, ${alpha1})`);
            gradient.addColorStop(1, `rgba(99, 179, 237, ${alpha2})`);
            
            ctx.strokeStyle = gradient;
            ctx.lineWidth = lineWidth;
            ctx.beginPath();
            ctx.moveTo(nodeIx, nodeIy);
            ctx.lineTo(nodeJ.x, nodeJ.y);
            ctx.stroke();
          }
        }
      }

      // Update and draw data pulses (optimized)
      for (let i = pulses.length - 1; i >= 0; i--) {
        const pulse = pulses[i];
        pulse.progress += pulse.speed;

        if (pulse.progress >= 1) {
          pulses.splice(i, 1);
          continue;
        }

        const fromNode = nodes[pulse.fromNode];
        const toNode = nodes[pulse.toNode];
        
        // Optimized interpolation
        const progress = pulse.progress;
        const x = fromNode.x + (toNode.x - fromNode.x) * progress;
        const y = fromNode.y + (toNode.y - fromNode.y) * progress;

        // Add current position to trail
        pulse.trail.push({ x, y, alpha: 1 });
        
        // Limit trail length and fade
        if (pulse.trail.length > 8) {
          pulse.trail.shift();
        }
        
        // Draw trail (optimized with cached calculations)
        const trailLength = pulse.trail.length;
        const invTrailLength = 1 / trailLength;
        for (let t = 0; t < trailLength; t++) {
          const trailPoint = pulse.trail[t];
          const trailRatio = t * invTrailLength;
          const trailAlpha = trailRatio * 0.4;
          const trailSize = 4 + trailRatio * 6;
          
          const trailGradient = ctx.createRadialGradient(
            trailPoint.x, trailPoint.y, 0,
            trailPoint.x, trailPoint.y, trailSize
          );
          const trailColor = pulse.color.replace(/[\d.]+\)$/g, `${trailAlpha})`);
          trailGradient.addColorStop(0, trailColor);
          trailGradient.addColorStop(1, 'rgba(0, 0, 0, 0)');
          ctx.fillStyle = trailGradient;
          const trailSize2 = trailSize * 2;
          ctx.fillRect(
            trailPoint.x - trailSize,
            trailPoint.y - trailSize,
            trailSize2,
            trailSize2
          );
        }

        // Draw pulse glow (enhanced)
        const glowSize = 10;
        const gradient = ctx.createRadialGradient(x, y, 0, x, y, glowSize);
        gradient.addColorStop(0, pulse.color);
        gradient.addColorStop(0.5, pulse.color.replace(/[\d.]+\)$/g, '0.4)'));
        gradient.addColorStop(1, 'rgba(0, 0, 0, 0)');
        ctx.fillStyle = gradient;
        const glowSize2 = glowSize * 2;
        ctx.fillRect(x - glowSize, y - glowSize, glowSize2, glowSize2);

        // Draw pulse core (brighter)
        ctx.fillStyle = pulse.color.replace(/[\d.]+\)$/g, '1)');
        ctx.beginPath();
        ctx.arc(x, y, 1.5, 0, PI2);
        ctx.fill();
      }

      // Draw nodes (sorted by depth for proper layering)
      // Only re-sort every 60 frames to improve performance (depth doesn't change)
      if (frameCountRef.current % 60 === 0 || sortedNodesRef.current.length !== nodesLength) {
        sortedNodesRef.current = [...nodes].sort((a, b) => a.depth - b.depth);
      }
      frameCountRef.current++;
      
      const sortedNodes = sortedNodesRef.current;
      const sortedNodesLength = sortedNodes.length;
      
      for (let i = 0; i < sortedNodesLength; i++) {
        const node = sortedNodes[i];
        
        // Skip invisible nodes early
        if (node.alphaMultiplier === 0) continue;
        
        const pulse = Math.sin(node.pulsePhase) * 0.25 + 0.75;
        const nodeDepth = node.depth;
        const depthAlpha = (0.6 + nodeDepth * 0.4) * node.alphaMultiplier;
        const nodeX = node.x;
        const nodeY = node.y;
        const nodeRadius = node.radius;
        
        // Enhanced node glow with depth
        const glowRadius = nodeRadius * (3 + nodeDepth * 2);
        const gradient = ctx.createRadialGradient(nodeX, nodeY, 0, nodeX, nodeY, glowRadius);
        const pulseDepthAlpha = pulse * depthAlpha;
        gradient.addColorStop(0, `rgba(14, 116, 144, ${0.35 * pulseDepthAlpha})`);
        gradient.addColorStop(0.4, `rgba(14, 116, 144, ${0.15 * pulseDepthAlpha})`);
        gradient.addColorStop(1, 'rgba(14, 116, 144, 0)');
        ctx.fillStyle = gradient;
        ctx.beginPath();
        ctx.arc(nodeX, nodeY, glowRadius, 0, PI2);
        ctx.fill();

        // Node core with depth-based brightness (optimized with bit shift)
        const coreColor = 99 + ((nodeDepth * 60) | 0);
        ctx.fillStyle = `rgba(${coreColor}, ${coreColor + 80}, 237, ${pulseDepthAlpha})`;
        ctx.beginPath();
        ctx.arc(nodeX, nodeY, nodeRadius, 0, PI2);
        ctx.fill();

        // Bright center (more prominent on closer nodes)
        ctx.fillStyle = `rgba(255, 255, 255, ${0.5 * pulseDepthAlpha})`;
        ctx.beginPath();
        ctx.arc(nodeX, nodeY, nodeRadius * (0.35 + nodeDepth * 0.15), 0, PI2);
        ctx.fill();
        
        // Subtle outer ring for depth (only for closer nodes)
        if (nodeDepth > 0.5) {
          ctx.strokeStyle = `rgba(99, 179, 237, ${0.3 * pulse * nodeDepth * node.alphaMultiplier})`;
          ctx.lineWidth = 0.5;
          ctx.beginPath();
          ctx.arc(nodeX, nodeY, nodeRadius * 1.3, 0, PI2);
          ctx.stroke();
        }
      }

      // Debug: Draw exclusion zones
      if (debugZones) {
        for (const zone of exclusionZones) {
          ctx.strokeStyle = 'rgba(255, 0, 0, 0.5)';
          ctx.lineWidth = 2;
          ctx.strokeRect(zone.x, zone.y, zone.width, zone.height);
          ctx.fillStyle = 'rgba(255, 0, 0, 0.1)';
          ctx.fillRect(zone.x, zone.y, zone.width, zone.height);
        }
      }

      // Create new pulses
      createDataPulse(nodes);

      animationRef.current = requestAnimationFrame(animate);
    };

    // Static render for reduced motion (optimized)
    const drawStatic = (ctx: CanvasRenderingContext2D, width: number, height: number) => {
      ctx.clearRect(0, 0, width, height);
      
      const nodes = nodesRef.current;
      if (nodes.length === 0) {
        nodesRef.current = initNodes(width, height);
        return;
      }

      // Draw connections with depth - optimized
      const connectionDistSq = connectionDistSqRef.current;
      const invConnectionDistance = 1 / connectionDistance;
      const nodesLength = nodes.length;
      const PI2 = Math.PI * 2;
      
      for (let i = 0; i < nodesLength; i++) {
        const nodeI = nodes[i];
        const nodeIx = nodeI.x;
        const nodeIy = nodeI.y;
        const nodeIDepth = nodeI.depth;
        
        for (let j = i + 1; j < nodesLength; j++) {
          const nodeJ = nodes[j];
          const dx = nodeIx - nodeJ.x;
          const dy = nodeIy - nodeJ.y;
          const distSq = dx * dx + dy * dy;
          
          if (distSq < connectionDistSq) {
            const dist = Math.sqrt(distSq);
            const distRatio = 1 - dist * invConnectionDistance;
            const avgDepth = (nodeIDepth + nodeJ.depth) * 0.5;
            const alpha = distRatio * 0.08 * (0.6 + avgDepth * 0.4);
            
            ctx.strokeStyle = `rgba(99, 179, 237, ${alpha})`;
            ctx.lineWidth = 0.3 + distRatio * 0.5 * avgDepth;
            ctx.beginPath();
            ctx.moveTo(nodeIx, nodeIy);
            ctx.lineTo(nodeJ.x, nodeJ.y);
            ctx.stroke();
          }
        }
      }

      // Draw nodes sorted by depth (cached sort)
      if (sortedNodesRef.current.length !== nodesLength) {
        sortedNodesRef.current = [...nodes].sort((a, b) => a.depth - b.depth);
      }
      const sortedNodes = sortedNodesRef.current;
      const sortedNodesLength = sortedNodes.length;
      
      for (let i = 0; i < sortedNodesLength; i++) {
        const node = sortedNodes[i];
        const nodeDepth = node.depth;
        const depthAlpha = 0.5 + nodeDepth * 0.3;
        const nodeX = node.x;
        const nodeY = node.y;
        const nodeRadius = node.radius;
        
        // Node glow
        const glowRadius = nodeRadius * 2;
        const gradient = ctx.createRadialGradient(nodeX, nodeY, 0, nodeX, nodeY, glowRadius);
        gradient.addColorStop(0, `rgba(14, 116, 144, ${0.2 * depthAlpha})`);
        gradient.addColorStop(1, 'rgba(14, 116, 144, 0)');
        ctx.fillStyle = gradient;
        ctx.beginPath();
        ctx.arc(nodeX, nodeY, glowRadius, 0, PI2);
        ctx.fill();
        
        // Node core
        ctx.fillStyle = `rgba(99, 179, 237, ${0.6 * depthAlpha})`;
        ctx.beginPath();
        ctx.arc(nodeX, nodeY, nodeRadius, 0, PI2);
        ctx.fill();
        
        // Center highlight
        ctx.fillStyle = `rgba(255, 255, 255, ${0.3 * depthAlpha})`;
        ctx.beginPath();
        ctx.arc(nodeX, nodeY, nodeRadius * 0.4, 0, PI2);
        ctx.fill();
      }
    };

    animate();

    return () => {
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current);
      }
      window.removeEventListener('resize', resize);
      if (interactive) {
        canvas.removeEventListener('mousemove', handleMouseMove);
        canvas.removeEventListener('mouseleave', handleMouseLeave);
      }
    };
  }, [nodeCount, particleCount, connectionDistance, interactive, intensity, prefersReducedMotion, params, exclusionZones]);

  return (
    <canvas
      ref={canvasRef}
      className={`absolute inset-0 w-full h-full pointer-events-none ${className}`}
      style={{ 
        mixBlendMode: 'screen',
        transform: 'translateZ(0)',
        willChange: 'contents'
      }}
    />
  );
};

export default NeuralBackground;

