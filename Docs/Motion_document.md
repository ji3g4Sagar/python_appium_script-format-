# class [swipePage]

* Description: 針對手機畫面中,執行上下左右滑動的動作.

# swipePage.swipePage(driver)

* Args: 
1. driver(necessary): webdriver的物件,來自於apkVersionAndCellConfig.py這個class

* useage:
anyname = swipe(driver)

# swipePage.swipeUp([t,n,xStart,yStart,yEnd])

* Des: 在頁面中向上滑動的動作

* Args:
1. t(option):預設值為400ms, 用來決定這個滑動所花費的時間
2. n(option):預設值為1, 用來決定這個滑動的次數
3. xStart(option):預設值為0.5, 表示起始滑動點為Ｘ軸的一半（0.5), 範圍為0.1 ~ 1
4. yStart(option):預設值為0.75, 表示起始滑動點為Y軸的0.75處開始, 範圍為0.1 ~ 1
5. yEnd(option):預設值為0.3, 滑動結束點為Ｙ軸的0.3處, 範圍為0.1 ~ 1

# swipePage.swipeDown([t,n,xStart,yStart,yEnd])

* Des: 在頁面中向下滑動的動作

* Args:
1. t(option):預設值為400ms, 用來決定這個滑動所花費的時間
2. n(option):預設值為1, 用來決定這個滑動的次數
3. xStart(option):預設值為0.5, 表示起始滑動點為Ｘ軸的一半（0.5), 範圍為0.1 ~ 1
4. yStart(option):預設值為0.3, 表示起始滑動點為Y軸的0.75處開始, 範圍為0.1 ~ 1
5. yEnd(option):預設值為0.75, 滑動結束點為Ｙ軸的0.3處, 範圍為0.1 ~ 1

# swipeLeft.swipeLeft([t,n,yStart,xStart,xEnd])

* Des: 在頁面中向左滑的動作

* Args:
1. t(option):預設值為400ms, 用來決定這個滑動所花費的時間
2. n(option):預設值為1, 用來決定這個滑動的次數
3. yStart(option):預設值為0.5, 表示起始滑動點為Y軸的0.5處開始, 範圍為0.1 ~ 1
4. xStart(option):預設值為0.8, 表示起始滑動點為Ｘ軸的0.8處, 範圍為0.1 ~ 1
5. xEnd(option):預設值為0.05, 滑動結束點為X軸的0.05處, 範圍為0.1 ~ 1

# swipePage.swipeRight([t,n,yStart,xStart,xEnd])

* Des: 在頁面中向右滑的動作

* Args:
1. t(option):預設值為400ms, 用來決定這個滑動所花費的時間
2. n(option):預設值為1, 用來決定這個滑動的次數
3. yStart(option):預設值為0.5, 表示起始滑動為Ｙ軸的0,5處開始, 範圍為0.1 ~ 1
4. xStart(option):預設值為0.1, 表示起始滑動為Ｘ軸的0.1處開始, 範圍為0.1 ~ 1
5. xEnd(option):預設值為0.75, 表示滑動結束為Ｘ軸的0.75處, 範圍為0.1 ~ 1

------

# class [enterContext]

* Description: 選擇手機元件中的特定元素, 並輸入指定文字

# enterContext.enterContext(driver)

* Des: 建構子

* Args: 
1. driver(necessary): webdriver的物件,來自於apkVersionAndCellConfig.py這個class

# enterContext.enter(context, resource_id)

* Des: 利用元素id來選擇特定的元件,做文字的輸入

* Args:
1. context(necessary):要輸入的文字內容
2. resource_id(necessary): 要選擇做輸入的元素id

# enterContext.enterSelectByTextviewText(context, textviewText)

* Des: 利用Textview上預設顯示的文字當作為選擇依據,選擇到元件做輸入

* Args:
1. context(necessary):要輸入的文字內容
2. textviewText(necessary):

------

# class [click]

* Description: 點擊手機上的元件

# click.click(driver)

* Des: 建構子

* Args:
1. driver(necessary): webdriver的物件,來自於apkVersionAndCellConfig.py這個class

# clickByResourceID(resource_id)

* Des: 利用手機元件的id來點擊特定元件

* Args: 
1. resource_id(necessary): 要被點擊的元件id

# clickByString(targetString)

* Des: 點擊含有特定文字的元件

* Args:
1. targetString(necessary): 被點擊的元件上所包含的文字內容

# clickFromManyThingsByResourceID(resources_id, index)

* Des: 點擊多個擁有相同元件id中的特定元件

* Args: 
1. resources_id(necessary): 要被點擊的元件id
2. index(necessary): 被點擊的元件索引, 索引值從0開始

-------

# class [waittingFor]

* Description: 等待操作後的特定元件出現,避免操作速度過快造成錯誤

# waittingFor.waittingFor(driver)

* Des: 建構子

* Args:
1. driver(necessary): webdriver的物件,來自於apkVersionAndCellConfig.py這個class

# waittingFor.implicitWait([time])

* Des: 等待特定時間

* Args:
1. time(option): 等待的時間,以秒為單位,預設為5秒

# waittingFor.explicitWaitByResourceID(resource_id, [index, time, frequecy])

* Des: 等待手機上特定元件出現

* Args:
1. resource_id(necessary): 要等待的特定元件id
2. index(option): 方法的模式設定,
	+ 預設為-1表示要等待的元件id為唯一
	+ 其他任意數字表示要等待的元件id有多個, 數字表示要等待的元素索引值
3. time(option): 等待的時間,單位為秒,預設為30秒
4. frequncy(option): 檢查特定元素是否存在的頻率, 單位為秒,預設為1秒

------

# class [getToast]

* Description: 找尋手機上顯示的Tost訊息

# getTost.getToast(driver)

* Des: 建構子

* Args:
1. driver(necessary): webdriver的物件,來自於apkVersionAndCellConfig.py這個class

# search4Toast(toastMessage)

* Des: 找尋有特定文字的Toast訊息

* Args: 
1. toastMessage(necessary): 要找尋的Toast顯示的文字內容

------

# class [findSpecificText]

* Description: 找尋包含特定文字的元件是否存在

# findSpecificText.findSpecificText(driver)

* Des: 建構子

* Args:
1. driver(necessary): webdriver的物件,來自於apkVersionAndCellConfig.py這個class

# findText(targetText, [mode])

* Des: 透過文字找尋特定元件是否存在

* Args: 
1. targetText(necessary): 所有找尋的文字內容
2. mode(option): 用來決定這個函數的回傳值
	+ 預設為0表示回傳值為找尋到的元件driver物件
	+ mode傳入值為1,表示回傳值為True/False

# findSpecificItemByResourceID(targetId [mode, index])

* Des: 利用元件id找尋特定物件

* Args:
1. targetId(necessary):要找尋的目標物件id
2. mode(option):決定這個函數的回傳值
	+ 預設為0表示回傳值為找尋到的元件driver物件
	+ mode傳入值為1,表示回傳值為True/False
3. index(option):找尋的物件是否唯一設定,
	+ 預設為-1表示要等待的元件id為唯一
	+ 其他任意數字表示要等待的元件id有多個, 數字表示要找尋的元素索引值

------

# class [getXYLocation]

* Description: 取得特定物件的X、Y座標

# getXYLocation.getXYLocation(driver)

* Des: 建構子

* Args:
1. driver(necessary): webdriver的物件,來自於apkVersionAndCellConfig.py這個class

# getXYByResourceID(resource_id, [index])

* Des: 透過元件id取得特定的元件Ｘ、Ｙ座標

* Args: 
1. resource_id(necessary): 要取得Ｘ、Ｙ座標的元件id
2. index(option):找尋的物件是否唯一設定
	+ 預設為-1表示要等待的元件id為唯一
	+ 其他任意數字表示要等待的元件id有多個, 數字表示要找尋的元素索引值




















