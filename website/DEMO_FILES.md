# Demo Files Feature

## Overview

The Demo Files page provides access to all company data files, including internal documents, reports, and datasets. This feature is designed for demonstration and internal access purposes.

## Features

- **File Browser**: Tree-view navigation of all data files organized by department
- **File Viewer**: In-browser preview of file contents (CSV, JSON, HTML, Markdown, etc.)
- **Search**: Filter files by name across all directories
- **File Details**: View file size, extension, and path information
- **Download**: Download individual files directly from the browser

## File Structure

All files are organized by department:

- **finance/**: Financial data including invoices, orders, and reports
- **hr-legal/**: Employee data, policies, benefits, and legal documents
- **product/**: Product information, meetings, memos, and projects
- **sales-marketing/**: Customer data, campaigns, leads, and marketing materials
- **public/**: Public-facing documents (product specs, guides, forms)

## Usage

### Accessing Demo Files

1. Click the "Demo Files" button in the navigation bar (orange button)
2. Browse files using the tree view on the left
3. Click any file to view its contents
4. Use the search bar to filter files by name
5. Download files using the download button in the file viewer

### Updating Data Files

When data files in the `/data` directory are updated, run:

```bash
npm run update-demo-files
```

This script will:
1. Copy all files from `/data` to `/public/data`
2. Regenerate the file tree JSON structure
3. Make all files accessible to the demo page

## Technical Details

### File Organization

- Source files: `/data/`
- Public files: `/website/public/data/`
- File tree: `/website/src/data/file_tree.json`

### Components

- **DemoFiles.tsx**: Main page component with file browser and viewer
- **file_tree.json**: Hierarchical structure of all data files
- **generate_file_tree.py**: Script to generate the file tree JSON
- **update_demo_files.sh**: Convenience script to sync and update files

### Supported File Types

The viewer automatically detects and displays:
- JSON files (syntax highlighted)
- CSV files (tabular data)
- Markdown files (formatted text)
- HTML files (source code)
- Plain text files

## Privacy Considerations

⚠️ **Important**: All files in the `/data` directory will be publicly accessible through the demo page. Ensure that:

1. No sensitive production data is included
2. All data is anonymized or synthetic
3. The demo page is only accessible in demo/development environments

## Maintenance

### Adding New Files

1. Add files to the appropriate directory in `/data`
2. Run `npm run update-demo-files` to sync
3. Files will automatically appear in the demo browser

### Removing Files

1. Delete files from `/data`
2. Run `npm run update-demo-files` to sync
3. Files will be removed from the demo browser

## Styling

The Demo Files page follows the same design system as other pages:
- Glass-morphism effects
- Gradient accents
- Smooth animations
- Responsive layout
- Dark theme optimized

