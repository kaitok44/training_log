## アプリケーション名
Training Log

## アプリケーション概要
日々の筋肉トレーニングを記録できる簡単なアプリです。

## 使用技術
Python 3.13.0　　
Django 5.0.10　　
PostgreSQL 14.17　　
Bootstrap v5.3.3　　
Git, Github　　

## テスト用アカウント
Username: test  
Password: testpassword

## 利用方法
ExerciseでAdd New Exerciseをクリックし行ったトレーニング種目名、どの筋肉をトレーニングしたかを選択し追加します。  
WorkoutsでAdd New Sessionをクリックし、その日のジムセッションを追加し、そこからその日行ったトレーニング種目を１セット毎に追加します。  

## このアプリを作成した理由
自身が日々ジムで行ったウェイトトレーニングを簡単に記録できるようなアプリが欲しかったため、作りました。

## よかった点
トレーニングを記録する際に必要最低限な機能は作れたと思います。

## 苦労した点
すべて自作だっため、どこから始めたらいいか分からずでした。　　
コーディングする前にどういう機能がほしいのか、それに必要なpageやclass、全て洗い出してからコーディングしました。　　
当初は日付を選択してその日のWorkoutが見れるようなものを目指したのですが、どうしてもうまくいかず結果新たなclass, Workout Session
を作って全てのWorkoutの一覧が見れるように変更しました。　　
また、一つのWebページに必要なデータをどう引っ張ってくるかに苦労しました。この場合に、どのclassのpkが必要なのかにものすごく調べる時間がかかりました。　　
