let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

python3 << EOF
import sys
from os.path import normpath, join
import vim
plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python'))
sys.path.insert(0, python_root_dir)
EOF


function! GenerateTestFile()
    python3 import generateTest
    python3 generateTest.main()
endfunction
command! -nargs=0 GenerateTestFile call GenerateTestFile()
