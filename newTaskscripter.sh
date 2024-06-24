#!/bin/bash
echo "File name?"
read file
echo -e "#!/usr/bin/env python3\n# $file\n\n\"\"\" Pagination Exercises \"\"\"" > $file
chmod u+x $file
vim $file
