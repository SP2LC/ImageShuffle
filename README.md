#Shuffle.py -Proggramming Conetst maked Problem Image-

####What is these source?
- shuffle.py  
特定の画像をシャッフルして問題画像を作るプログラム

####how to run
` python shuffle.py [元画像.png] [横分割数] [縦分割数] [シード値(オプション)] `  
元画像.pngを横分割数と縦分割数に従ってランダムにシャッフルして問題画像として出力します。  
実際にはシャッフルパターンは一定になってしまうので同じ分割数で作る場合はシード値をいじってね  
受け付ける画像サイズは'1024 * 1024'まで、ピクセル数と分割数の約数が一致しないと分割できない。  



####how to install

If you don't have `pip` in your python enviroment, first `easy_install pip`  
If you don't have `easy_install` in your python enviroment to, please install `easy_install` on your package system.

- ` pip install numpy `

- ` pip install pil `  
-- If you get error message about '(use --allow-external pil)' , please install with ` pip install pil --allow-external pil --allow-unverified pil `


- ` pip isntall matplotlib `

####how to convet images

If you don't have ` imagemagick ` in your homebrew enviroment, first `brew install imagemagick`  

- `convert -geometry [横ピクセル]x[縦ピクセル] [変換する.JPG] [変換後.PNG]`  
  
横縦比をを変えて変換んする場合は  

- `convert -geometry [横ピクセル]x[縦ピクセル]! [変換する.JPG] [変換後.PNG]`


########README CHECKE AT `http://markdownlivepreview.com`