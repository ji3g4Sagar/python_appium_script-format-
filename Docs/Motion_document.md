# class [swipePage]
## Description
* 針對手機畫面中,執行上下左右滑動的動作.

### swipePage.swipePage(driver)

* Args: 
1. driver(necessary): webdriver的物件,來自於apkVersionAndCellConfig.py這個class

#### useage:
anyname = swipe(driver)


### swipePage.swipeUp([t,n,xStart,yStart,yEnd])

* Args:
1. t(option):預設值為400ms, 用來決定這個滑動所花費的時間
2. n(option):預設值為1, 用來決定這個滑動的次數
3. xStart(option):預設值為0.5, 表示起始滑動點為Ｘ軸的一半（0.5), 範圍為0.1 ~ 1
4. yStart(option):預設值為0.75, 表示起始滑動點為Y軸的0.75處開始, 範圍為0.1 ~ 1
5. yEnd(option):預設值為0.3, 滑動結束點為Ｙ軸的0.3處, 範圍為0.1 ~ 1
