# Robotix Website

A showcase for the Robotix dataset.

## Features

- **Product Catalog**: Browse and filter through our comprehensive robotics product line
- **Customer Portal**: View orders, support tickets, and account analytics
- **Documentation Center**: Access technical specifications, user guides, and policies
- **Support System**: Submit support requests and view FAQs
- **Company Information**: Learn about our mission, values, and team

## Tech Stack

- **React 19** - UI framework
- **TypeScript** - Type-safe development
- **Vite** - Fast build tool and dev server
- **React Router** - Client-side routing
- **Tailwind CSS** - Utility-first styling
- **Recharts** - Data visualization
- **Lucide React** - Icon library

## Getting Started

### Installation

```bash
npm install
```

### Development

Start the development server:

```bash
npm run dev
```

The site will be available at `http://localhost:5173`

### Build

Create a production build:

```bash
npm run build
```

### Preview

Preview the production build:

```bash
npm run preview
```

## Project Structure

```
website/
├── src/
│   ├── components/      # Reusable components
│   │   └── Layout.tsx   # Main layout with nav and footer
│   ├── pages/           # Page components
│   │   ├── Home.tsx
│   │   ├── Products.tsx
│   │   ├── ProductDetail.tsx
│   │   ├── CustomerPortal.tsx
│   │   ├── Documentation.tsx
│   │   ├── Support.tsx
│   │   ├── Company.tsx
│   │   └── NotFound.tsx
│   ├── data/            # JSON data files
│   ├── types/           # TypeScript type definitions
│   ├── App.tsx          # Main app component with routing
│   ├── main.tsx         # Entry point
│   └── index.css        # Global styles
├── index.html           # HTML template
├── vite.config.ts       # Vite configuration
├── tailwind.config.js   # Tailwind CSS configuration
└── tsconfig.json        # TypeScript configuration
```

## Pages

- **Home** - Hero section, featured products, company overview
- **Products** - Searchable product catalog with filtering and sorting
- **Product Detail** - Individual product information and specifications
- **Customer Portal** - Customer dashboard with orders and support tickets
- **Documentation** - Browse and search technical documentation
- **Support** - Submit support requests and view FAQs
- **Company** - About us, mission, values, and team information

## Data

The website uses JSON data files sourced from the parent `data/` directory:
- `products.json` - Product catalog
- `customers.json` - Customer information
- `orders.json` - Order data
- `order_items.json` - Order line items
- `support_tickets.json` - Support ticket history
- `employees.json` - Employee information
- `metadata.json` - Document metadata

## Styling

The website uses Tailwind CSS with a custom configuration featuring:
- Primary and secondary color palettes
- Custom animations (fade-in, slide-up, slide-down)
- Responsive design for all screen sizes
- Glass morphism effects
- Custom utility classes

## License

© 2024 Robotix. All rights reserved.
