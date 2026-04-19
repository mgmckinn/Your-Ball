#!/bin/bash

# Install Your Ball Theme as a VS Code Extension

echo "🎨 Installing Your Ball - Vibrant Theme..."

# Create extension directory
EXTENSION_DIR="$HOME/.vscode/extensions/your-ball-theme"
mkdir -p "$EXTENSION_DIR/themes"

# Copy theme file
cp "$(dirname "$0")/your-ball-theme.json" "$EXTENSION_DIR/themes/"

# Create package.json
cat > "$EXTENSION_DIR/package.json" << 'EOF'
{
  "name": "your-ball-theme",
  "displayName": "Your Ball - Vibrant",
  "description": "A vibrant electric blue/purple/cyan color theme inspired by the Your Ball app",
  "version": "1.0.0",
  "publisher": "your-ball",
  "engines": {
    "vscode": "^1.70.0"
  },
  "categories": ["Themes"],
  "keywords": ["theme", "color-theme", "dark", "vibrant", "purple", "cyan", "blue"],
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
EOF

echo "✅ Theme installed successfully!"
echo ""
echo "📝 Next steps:"
echo "   1. Reload VS Code (Cmd+Shift+P → 'Developer: Reload Window')"
echo "   2. Open Command Palette (Cmd+Shift+P)"
echo "   3. Type 'Color Theme'"
echo "   4. Select 'Your Ball - Vibrant'"
echo ""
echo "🎨 Enjoy your new theme!"
