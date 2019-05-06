#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
#                                                                             #
# RMG - Reaction Mechanism Generator                                          #
#                                                                             #
# Copyright (c) 2002-2019 Prof. William H. Green (whgreen@mit.edu),           #
# Prof. Richard H. West (r.west@neu.edu) and the RMG Team (rmg_dev@mit.edu)   #
#                                                                             #
# Permission is hereby granted, free of charge, to any person obtaining a     #
# copy of this software and associated documentation files (the 'Software'),  #
# to deal in the Software without restriction, including without limitation   #
# the rights to use, copy, modify, merge, publish, distribute, sublicense,    #
# and/or sell copies of the Software, and to permit persons to whom the       #
# Software is furnished to do so, subject to the following conditions:        #
#                                                                             #
# The above copyright notice and this permission notice shall be included in  #
# all copies or substantial portions of the Software.                         #
#                                                                             #
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,    #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER      #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING     #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER         #
# DEALINGS IN THE SOFTWARE.                                                   #
#                                                                             #
###############################################################################

import os
import shutil
import subprocess


fam_dir = os.path.abspath('../input/kinetics/families')
dir_list = os.listdir(fam_dir)
fam_list = sorted([item for item in dir_list if os.path.isdir(os.path.join(fam_dir, item))])  # Only keep folders

img_dir = os.path.abspath('./temp/images')
if not os.path.isdir(img_dir):
    os.makedirs(img_dir)

latex_header = r"""\documentclass{article}

\usepackage[margin=1in]{geometry}
\usepackage{graphicx,color}
\graphicspath{{""" + img_dir + '/' + r"""}}
\usepackage{epstopdf}

\begin{document}

\begin{center}
\huge
RMG-Py Reaction Families
\end{center}

"""

latex_footer = r"""
\end{document}
"""

if not os.path.isdir('./temp/images'):
    os.makedirs('./temp/images')

with open('./temp/rmg_reaction_families.tex', 'w') as f:
    f.write(latex_header)
    for fam in fam_list:
        cleaned_name = fam.replace('_', '\_')
        f.write(r'\section*{{\texttt{{{0}}}}}'.format(cleaned_name))
        f.write('\n\n')
        img_file = os.path.join(fam_dir, fam, 'template.eps')
        f.write(r'\begin{center}')
        f.write('\n')
        if os.path.isfile(img_file):
            filename = fam + '.eps'
            new_file = os.path.join('./temp', 'images', filename)
            shutil.copyfile(img_file, new_file)
            f.write(r'\includegraphics[scale=0.8]{{{0}}}'.format(filename))
            f.write('\n')
        else:
            f.write(r'Image Not Available')
            f.write('\n')
        f.write(r'\end{center}')
        f.write('\n\n')

    f.write(latex_footer)

os.chdir('./temp')
subprocess.check_call(['pdflatex', '-shell-escape', '-interaction=nonstopmode', 'rmg_reaction_families.tex'])
shutil.copyfile('rmg_reaction_families.pdf', '../../rmg_reaction_families.pdf')
os.chdir('../')
shutil.rmtree('./temp')
