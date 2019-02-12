# class [swipePage]

## Description
* 針對手機畫面中,執行上下左右滑動的動作.

### swipePage.swipePage(driver)

* Args: 
1. driver(necessary): webdriver的物件,來自於apkVersionAndCellConfig.py這個class

* useage:
anyname = swipe(driver)

swipePage.swipeUp([t,n,xStart,yStart,yEnd])
====
* Des: 在頁面中向上滑動的動作

* Args:
1. t(option):預設值為400ms, 用來決定這個滑動所花費的時間
2. n(option):預設值為1, 用來決定這個滑動的次數
3. xStart(option):預設值為0.5, 表示起始滑動點為Ｘ軸的一半（0.5), 範圍為0.1 ~ 1
4. yStart(option):預設值為0.75, 表示起始滑動點為Y軸的0.75處開始, 範圍為0.1 ~ 1
5. yEnd(option):預設值為0.3, 滑動結束點為Ｙ軸的0.3處, 範圍為0.1 ~ 1

### swipePage.swipeDown([t,n,xStart,yStart,yEnd])

* Des: 在頁面中向下滑動的動作

* Args:
1. t(option):預設值為400ms, 用來決定這個滑動所花費的時間
2. n(option):預設值為1, 用來決定這個滑動的次數
3. xStart(option):預設值為0.5, 表示起始滑動點為Ｘ軸的一半（0.5), 範圍為0.1 ~ 1
4. yStart(option):預設值為0.3, 表示起始滑動點為Y軸的0.75處開始, 範圍為0.1 ~ 1
5. yEnd(option):預設值為0.75, 滑動結束點為Ｙ軸的0.3處, 範圍為0.1 ~ 1

### swipeLeft.swipeLeft([t,n,yStart,xStart,xEnd])

* Des: 在頁面中向左滑的動作

* Args:
1. t(option):預設值為400ms, 用來決定這個滑動所花費的時間
2. n(option):預設值為1, 用來決定這個滑動的次數
3. yStart(option):預設值為0.5, 表示起始滑動點為Y軸的0.5處開始, 範圍為0.1 ~ 1
4. xStart(option):預設值為0.8, 表示起始滑動點為Ｘ軸的0.8處, 範圍為0.1 ~ 1
5. xEnd(option):預設值為0.05, 滑動結束點為X軸的0.05處, 範圍為0.1 ~ 1

### swipePage.swipeRight([t,n,yStart,xStart,xEnd])

* Des: 在頁面中向右滑的動作

* Args:
1. t(option):預設值為400ms, 用來決定這個滑動所花費的時間
2. n(option):預設值為1, 用來決定這個滑動的次數
3. yStart(option):預設值為0.5, 表示起始滑動為Ｙ軸的0,5處開始, 範圍為0.1 ~ 1
4. xStart(option):預設值為0.1, 表示起始滑動為Ｘ軸的0.1處開始, 範圍為0.1 ~ 1
5. xEnd(option):預設值為0.75, 表示滑動結束為Ｘ軸的0.75處, 範圍為0.1 ~ 1

-------------------------------------------------------------------

# class [enterContext]

## Description
* 選擇手機元件中的特定元素, 並輸入指定文字

### enterContext.enterContext(driver)

* Args: 
1. driver(necessary): webdriver的物件,來自於apkVersionAndCellConfig.py這個class

### enterContext.enter(context, resource_id)

* Args:
1. context(necessary):要輸入的文字內容
2. resource_id(necessary): 要選擇做輸入的元素id

### enterContext.enterSelectByTextviewText(context, textviewText)

* Args:
1. context(necessary):要輸入的文字內容
2. textviewText(necessary):









