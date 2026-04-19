<!-- @format -->

# Your Ball - Vibrant VS Code Theme 🎨

A vibrant, modern VS Code theme inspired by your app's electric blue, purple, pink, and cyan color scheme!

## Installation

### Option 1: Quick Setup (Current Workspace Only)

1. The theme file is already in `.vscode/your-ball-theme.json`
2. Open VS Code Command Palette (`Cmd+Shift+P` or `Ctrl+Shift+P`)
3. Type: `Preferences: Color Theme`
4. Scroll down and click on `Browse Additional Color Themes...`
5. At the bottom of the list, you should see custom themes from your workspace

### Option 2: Install as VS Code Extension (Recommended)

To use this theme globally in VS Code:

1. **Create the extension structure:**

   ```bash
   mkdir -p ~/.vscode/extensions/your-ball-theme
   cd ~/.vscode/extensions/your-ball-theme
   ```

2. **Copy the theme file:**

   ```bash
   cp "/Users/mitchellmckinney/Your Ball/.vscode/your-ball-theme.json" ./themes/
   ```

3. **Create package.json:**

   ```json
   {
     "name": "your-ball-theme",
     "displayName": "Your Ball - Vibrant",
     "description": "A vibrant blue/purple/cyan theme",
     "version": "1.0.0",
     "engines": {
       "vscode": "^1.70.0"
     },
     "categories": ["Themes"],
     "contributes": {
       "themes": [
         {
           "label": "Your Ball - Vibrant",
           "uiTheme": "vs-dark",
           "path": "./themes/your-ball-theme.json"
         }
       ]
     }
   }
   ```

4. **Reload VS Code** and select the theme from the color theme picker

### Option 3: Publish to VS Code Marketplace

Want to share with others?

1. Install vsce: `npm install -g @vscode/vsce`
2. Package: `vsce package`
3. Publish: `vsce publish`

## Color Palette

- **Background**: `#1e1b4b` (Deep Purple)
- **Primary**: `#00f2fe` (Electric Cyan)
- **Secondary**: `#f093fb` (Pink)
- **Accent**: `#667eea` (Blue Purple)
- **Highlight**: `#4facfe` (Sky Blue)

## Features

✨ Vibrant electric colors that pop  
🎨 Optimized for JavaScript, TypeScript, React, CSS, HTML, and Markdown  
🌈 Beautiful syntax highlighting with the Your Ball color scheme  
💜 Purple-themed UI elements  
🔵 Cyan accents throughout  
💖 Pink highlights for important elements

## Screenshots

The theme includes:

- Electric cyan text on deep purple background
- Pink keywords and properties
- Blue functions and classes
- Gradient-inspired status bar and activity bar
- Cyan terminal colors

## Customization

Want to tweak colors? Edit `.vscode/your-ball-theme.json` and reload VS Code!

## Feedback

Love the theme? Consider publishing it to the VS Code Marketplace so others can enjoy it too!
