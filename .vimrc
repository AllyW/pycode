" Configuration file for vim
set modelines=0		" CVE-2007-2438
runtime autoload/pathogen.vim
execute pathogen#infect()
filetype off
"set rtp+=~/.vim/bundle/Vundle.vim
"call vundle#begin()
"Plugin 'gmarik/vundle'
"Plugin 'git://git.wincent.com/command-t.git'
"Bundle 'Valloric/YouCompleteMe'
"call vundle#end()

" Normally we use vim-extensions. If you want true vi-compatibility
"let g:ycm_global_ycm_extra_conf = '~/.vim/bundle/YouCompleteMe/cpp/ycm/.ycm_extra_conf.py'




" remove change the following statements
set nocompatible	" Use Vim defaults instead of 100% vi compatibility
set backspace=2		" more powerful backspacing

syntax on

autocmd InsertEnter * se cul
set smartindent
set autoindent
set confirm
set tabstop=4
set softtabstop=4
set shiftwidth=4
set noexpandtab
set smarttab
set number
set history=50

set hlsearch
set incsearch

set gdefault
set encoding=utf-8
set fenc=utf-8
set helplang=cn
set background=dark
let g:solorized_termcolors=256
colorscheme solarized

"colorscheme Distinguished
set guifont=Monaco:h14


set cmdheight=2
set ruler
set showcmd

set showmatch
set matchtime=5
set lines=50 columns=120
set noerrorbells
set novisualbell


filetype plugin indent on

"let g:pydiction_location='Users/allywang/.vim/bundle/pydiction/complete-dict'


set whichwrap=b,s,<,>,[,]

set fileformat=mac

map <F5> :call CompileRunGcc()<CR>
func! CompileRunGcc()
    exec "w"
    if &filetype == 'c'
        exec "!gcc % -o %<"
        exec "! ./%<"
    elseif &filetype == 'cpp'
        exec "!g++ -std=c++11 % -o %<"
        exec "! ./%<"
    elseif &filetype == 'java' 
        exec "!javac %" 
        exec "!java %<"
    elseif &filetype == 'sh'
        :!./%
    elseif &filetype == 'python'
        exec "!python %"
    endif
endfunc

function! AutoClose()
	:inoremap ( ()<ESC>i
	:inoremap " ""<ESC>i
	:inoremap ' ''<ESC>i
	:inoremap ` ``<ESC>i
	:inoremap { {}<ESC>i
	:inoremap [ []<ESC>i
	:inoremap ) <c-r>=ClosePair(')')<CR>
	:inoremap } <c-r>=ClosePair('}')<CR>
	:inoremap ] <c-r>=ClosePair(']')<CR>
endf
 
function! ClosePair(char)
	if getline('.')[col('.') - 1] == a:char
		return "\<Right>"
	else
		return a:char
	endif
endf 

"inoremap ( ()<ESC>i
"inoremap [ []<ESC>i
"inoremap { {}<ESC>i
"inoremap < <><ESC>i
" 括号自动生成
au FileType cpp,css,html,python,javascript exe AutoClose()

" Don't write backup file if vim is being called by "crontab -e"
au BufWrite /private/tmp/crontab.* set nowritebackup nobackup
" Don't write backup file if vim is being called by "chpass"
au BufWrite /private/etc/pw.* set nowritebackup nobackup
