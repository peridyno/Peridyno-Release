# Peridyno Windows Qt Release Tutorial

## Prerequisites
- Visual Studio
- CMake  
- Qt
- Qt Install Framework

## Steps

1. **Compile Release Files**
   - Modify CMake: Set `PERIDYNO_ASSET_PATH` to `./data`
   - Purpose: Change to relative directory

2. **Deploy Qt Dependencies**
   - Open Qt Command Prompt (MSVC)
   - Navigate to Release folder
   - Run command: `windeployqt --release dynoQtGUI-1.2.1.dll`
   - Purpose: Search and supplement Qt dependencies

3. **Copy Files**
   - Copy all files from Release folder to:
   - `Windows-Qt/packages/com.peridyno/data` in this repository

4. **Create Installer**
   - Execute: `binarycreator --offline-only -c config/config.xml -p packages Peridyno-Qt-x.x.x-amd64-win -v`
