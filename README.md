# Korla Plus

**Korla Plus** is based on Korla, but with several additions, color changes, and other alterations made. As with Korla, there's you may need to update the icon cache. A script is included.

Different versions available:
* ***korla-plus*** - for dark themes with dark panel
* ***korla-light-plus*** - for light themes with dark panel (depends on Korla)
* ***korla-light-panel-plus*** - for light themes with light panel (depends on Korla and Korla-light)
* ***korla-prgey-plus*** - theme with grey folder colors (depends on Korla)

## Installation

Clone this repository on your system.
    git clone https://github.com/GabePoel/Korla-Plus.git

and copy ***korla***, ***korla-light*** and ***korla-light-panel*** subfolders to one of the following folders: 

* `/usr/share/icons/` - icons available system-wide
* `$HOME/.local/share/icons/` - icons only available to local user

Alternatively, you can use the included installation script in one of the following ways.

Use `python3 install.py link ` to create symbolic links to your icons for easy modifying.

Or use `python3 install.py move` to just move the included themes and then delete everything else.