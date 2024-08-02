#!/bin/bash
echo "File name?"
read file
echo -e "#!/usr/bin/env python3\n# $file\n\n\"\"\" i18n (Internationalization) Exercises \"\"\"" > $file
chmod u+x $file
vim $file
