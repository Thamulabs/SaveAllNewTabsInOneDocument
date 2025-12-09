# Save All New Tabs in One Document

A Sublime Text package that identifies all "new" unsaved tabs (tabs with content that have never been saved to a file), concatenates their content into a single file with separators, prompts you to save it, and then closes those tabs.

Useful for cleaning up a workspace cluttered with temporary scratchpads.

## Features

- Finds all tabs that are "dirty" and have no associated file path.
- Combines their content into one text block.
- Adds headers identifying the source tab name/ID.
- Prompts for a save location.
- Automatically closes the processed tabs upon successful save.
- Preserves existing file-backed buffers.

## Installation

### via Package Control
1. Open the **Command Palette** `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS).
2. Type `Install Package` and press Enter.
3. Search for `Save All New Tabs to One File` and press Enter.

### Manual Installation
1. Search for `Browse Packages` in the Command Palette.
2. Open the directory.
3. Clone this repository into that directory:
   ```bash
   git clone https://github.com/Thamulabs/SaveAllNewTabsInOneDocument.git
   ```

## Usage

1. Open the **Command Palette**.
2. Run `Save All New Tabs to One File`.
3. Choose a destination for the combined file.

## License

MIT License
