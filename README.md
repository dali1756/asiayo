## AsiaYo - Backend Engineer

### 題目一
### 請寫出一條查詢語句 (SQL),列出在 2023 年 5 月下訂的訂單,使用台幣付款且5月總金額最多的前 10 筆的旅宿 ID (bnb_id), 旅宿名稱 (bnb_name), 5 月總金額 (may_amount)
SELECT bnbs.bnb_id, bnbs.bnb_name, orders.SUM(amount) AS may_total_amount FROM bnbs JOIN orders ON bnbs.id = orders.bnb_id WHERE AND check_in_date >= "2024-05-01" AND check_out_date <= "2024-05-31" AND orders.currency = "TWD" GROUP BY bnbs.id, bnbs.name ORDER BY may_total_amount LIMIT 10;

### 題目二
### 在題目一的執行下,我們發現 SQL 執行速度很慢,您會怎麼去優化?請闡述您怎麼判斷與優化的方式
使用 index索引 的方式進行優化，舉個例子：在 members table 中有一百萬筆的資料，如果要透過特定搜尋方式查詢用戶，而 members table 中沒有 index索引，那就表示會根據整個 table 進行掃描，這樣會消耗掉很多時間和資源的浪費，以下用 SQL 語法說明：
CREATE TABLE members(
	id,
	name VARCHAR(255),
	email VARCHAR(255)
)
SELECT * FROM members WHERE id = 800000;
依照上方範例是沒有使用 index索引的，查詢時間約會在 0.05 秒左右，那麼下方使用 index索引 試試看
CREATE INDEX index_members_id ON members(id)
SELECT * FROM members WHERE id = 800000;
有加上 INDEX 後同樣的查詢結果時間變成約 0.00003 秒，使用索引方式優化原因是，就像是在看一本書，如果想快速的找到某主題，那直接看目錄查詢是最快的不用一頁一頁翻找就可以知道該主題在書中的哪一頁。而在資料庫中當對一個有索引的資料表進行查詢時，資料庫能用類似的方法快速定位到資料表中的位置進而減少查詢時間的浪費。