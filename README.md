# CoNR Dataset 
[简体中文README](https://github.com/P2Oileen/CoNR_Dataset#conr-数据集) [日本語README](https://github.com/P2Oileen/CoNR_Dataset#conr-データセット)

**[Google Drive Download Link](https://drive.google.com/drive/folders/1hadpzwt79SG8wS45_cbZKs9S5O0_nGlb?usp=share_link)**

This dataset is collected and produced by the GitHub project: IJCAI2023-CoNR.
This dataset consists of three parts: `annotation`, `model` and `motion`. This document is the collation instructions and agreement of the dataset. Original project address: [https://github.com/megvii-research/IJCAI2023-CoNR](https://github.com/megvii-research/IJCAI2023-CoNR).

This dataset is for research use only, **by downloading you agree to our rules**. We sincerely appreciate the work of all community authors.

## Data download and decompression
Please download all data from [**Google Drive download link**](https://drive.google.com/drive/folders/1hadpzwt79SG8wS45_cbZKs9S5O0_nGlb?usp=share_link). Among them, `CoNR_Dataset_3Dmodel_only_a*` is the 3D model data, `CoNR_Dataset_motion_only_a*` is the motion data, and `CoNR_Dataset_annotation_only.tar.gz` is the annotation data of the 2D image.

For data with multiple volumes, you need to connect them together before decompressing. Let's take 3D model data as an example:

```
cat CoNR_Dataset_3Dmodel_only_a* > model.tar.gz
tar -zxvf model.tar.gz
```

For `CoNR_Dataset_annotation_only.tar.gz`, just decompress it directly

```
tar -zxvf CoNR_Dataset_annotation_only.tar.gz
```

## 2D Image Annotation
This part involves the contents of `annotation` folder.

We provide segmentation and annotation data of images from the danbooru website. In order to maintain copyright security, we do not provide the file of the original image, only the annotation. You need to download the original image yourself.

### Original image download
Specifically, for a file under the `annotation` folder: 
`0a0f715b298cc59037ab4f317b97eb7a.jpg.npz`, please extract its prefix `0a0e` and organize it into `https://cdn.donmai.us/original/0a/0f/`. After that, please delete the suffix `.npz` of the file, and connect the remaining content with the url to get `https://cdn.donmai.us/original/0a/0f/0a0f715b298cc59037ab4f317b97eb7a.jpg`. This is the link to the original image.

### Annotation decompression
See `scripts/unzip_annotation.py`. We provide an example of decompressing annotations.

## motion/model
This part involves the contents of `motion` and `model` folders.

Please note: We respect the rights and interests of all MMD community producers, and the data sets provided are collected from public information on the Internet. Since some models/actions come from integrated packages circulating on the Internet, we cannot determine their original sources, nor can they be sure that they must contain the original README information. Nevertheless, we have manually verified each model containing README information (including confirming the terms of the specification given in the link). Our screening principles are as follows:

We do not publish:

1. Content that cannot be redistributed
2. Content that can only be edited and then redistributed
3. Content that can only be redistributed after contacting the author for authorization
4. Content that can only be used after contacting the author for authorization
5. Content that can only be republished privately
7. Content permitted only for use with MMD-related software
8. Content that contains README but cannot be decoded
9. Content with a README, but I can't understand it
10. Excessively sexual content

We publish:

1. Contents allowing various secondary posting
2. Contents without README, or are no longer accessible in terms of statutes given in the form of links
3. A modified model, which contains the README of the original model. The author of the original model allows redistribution after modification, but the modifier does not attach his own README.
4. Contents that redistribution is allowed, but not for commercial use
5. Contents that redistribution is allowed, but the original folder is not allowed to be modified
6. Open source contents under GNU terms
7. Contents that redistribution in non-Chinese regions is allowed, but redistribution in China is restricted (we promise to only publish on GitHub/GoogleDrive)
8. For content with various usage/redistributing conditions, we redistribute it under the usage conditions that meet the requirements of the original author (for example, attach a new README, attach the original link, etc., all of which are in `README_added_by_CoNR.txt`)

The author's foreign language level is average. When reading the README, although various translation tools are used as much as possible to determine the compliance of the redistribution, since the README often contains multiple languages, there may be some omissions. If there is a problem, we hereby express our sincere apologies and are willing to make timely revisions. Authors in the MMD community are welcome to supervise.

### Content additions and deletions
Due to the unreachable authors of many contents and the lack of manpower in CoNR, we are sorry that we are unable to contact all authors to confirm their willingness. `motion_model_SHA256.txt` in the root directory contains the SHA256 codes of all pmx/pmd/vmd files (deduplicated and sorted), which is convenient for community authors to view. If you find that you are the author of a certain content in the dataset and do not want your content to appear in it, please contact me: **huangailin@megvii.com / p2oileen@whu.edu.cn**. If you want to contribute your own content to the dataset, please contact me!

### Precautions for use
1. Please respect the labor achievements of MMD authors and follow the general rules agreed in the community. Specifically, when you use a motion or a model, please be sure to follow the original author's requirements (such as credit, etc.) in the README. CoNR authors are not responsible for any problems caused by improper use.
2. MMD model data and action data do not have a very common format, and various problems may occur. However, since the training of CoNR only uses these data to generate UDP and images, and does not require very strict motion accuracy requirements, I did not make modifications. If you have high requirements in this area, please filter or manually repair the model.
3. The motion data has not been carefully cleaned. Some .vmd files may be camera motion files or motion files of various accessories, please be careful to distinguish.

# CoNR 数据集

本数据集由GitHub项目：IJCAI2023-CoNR收集并制作，由三个部分组成：`annotation`，`model`和`motion`。本文件为数据集的整理说明和君子协定。
原项目地址：[https://github.com/megvii-research/IJCAI2023-CoNR](https://github.com/megvii-research/IJCAI2023-CoNR)。

该数据集仅供研究使用，**下载即代表您同意我们的规则**。我们真诚地感谢所有社区作者的工作。

## 数据下载和解压
所有数据请从[**Google Drive 下载链接**](https://drive.google.com/drive/folders/1hadpzwt79SG8wS45_cbZKs9S5O0_nGlb?usp=share_link)下载。其中，`CoNR_Dataset_3Dmodel_only_a*`为3D模型数据，`CoNR_Dataset_motion_only_a*`为动作数据，`CoNR_Dataset_annotation_only.tar.gz`为2D图像的标注数据。

对于有多个分卷的数据，你需要将它们连接到一起后再进行解压。我们以3D模型数据举例而言：

```
cat CoNR_Dataset_3Dmodel_only_a* > model.tar.gz
tar -zxvf model.tar.gz
```

对于`CoNR_Dataset_annotation_only.tar.gz`，直接解压即可

```
tar -zxvf CoNR_Dataset_annotation_only.tar.gz
```

## 2D图像标注
此部分涉及到`annotation`文件夹下的内容。

我们提供来自于danbooru网站的图像的分割标注数据。为了维护版权安全，我们不提供原图像的文件，只提供标注。您需要自行下载原图像。

### 原图像下载
具体而言，对于`annotation`文件夹下的一个文件：`0a0e3ae27041b1338aba7a4af58c313f.jpg.npz`，请提取出他的前缀`0a0e`，并组织成`https://cdn.donmai.us/original/0a/0e/`。之后，请删除该文件的后缀`.npz`，并将剩下的内容和url相连接，得到`https://cdn.donmai.us/original/0a/0e/0a0e3ae27041b1338aba7a4af58c313f.jpg`。这就是原图的链接。

### 标注解压
参见`scripts/unzip_annotation.py`。我们提供了一个为标注进行解压的示例。


## 动作数据和3D模型
此部分涉及到`motion`和`model`文件夹下的内容。

请注意：我们尊重所有MMD社区制作者的权益，所提供的数据集从互联网公开信息收集而来。由于一些模型/动作来自于网络流传的整合包，我们不能确定其最初始的来源，也不能确定其一定包含原始的README信息。尽管如此，我们已经人工逐项确认含有README信息的模型（包括确认了以链接给出的规约条款）。我们的筛选原则如下：

我们不发布：

1. 声明不可二次发布的内容
2. 声明只可以编辑后再进行二次发布的内容
3. 需要联系作者授权后才可以二次发布的内容
4. 需要联系作者授权后才可以使用的内容
5. 只接受链接形式的二次发布的内容
6. 只允许非公开性质的二次发布的内容
7. 只允许供MMD相关软件使用的内容
8. README无法解码的内容
9. 虽然有README，但是我看不懂的内容
10. 具有过度色情意味的内容

我们发布：

1. 允许各种二次发布的内容
2. 不含有README/以链接形式给出的规约条款已经不可访问的内容
3. 该数据为改模，含有原模型的README，原模型作者允许进行修改后二次配布，但修改者并没有附加自己的README的模型。
4. 允许二次发布，但不可用于商业用途的内容
5. 允许二次发布，但不允许修改原文件夹内容的内容
6. 遵循GNU条款进行开源的内容
7. 允许在非中国地区二次发布，但限制在中国地区二次发布的内容（我们承诺仅在GitHub/GoogleDrive上发布）
8. 具有各类使用/发布条件的内容，我们在满足原作者要求的使用条件下进行发布（例如，附上新的README，附上原链接等等，以上均在`README_added_by_CoNR.txt`中）

作者的外语水平一般，在读readme的时候，虽然尽可能使用了各类翻译工具来确定再次发布的合规性，由于README往往包含多种语言，可能会有一些疏漏。如果因此产生问题，我们在此表示诚挚的歉意，并愿意及时进行修改，欢迎MMD社区作者进行监督。

### 内容增删
由于很多内容的作者已不可考以及CoNR的人力缺乏，很抱歉我们无力向所有作者们联系确认意愿。根目录下的`motion_model_SHA256.txt` 包含所有pmx/pmd/vmd文件的SHA256码（已去重和排序），便于社区工作者们进行查看。如果你发现自己是数据集中某个内容的作者，且不希望您的内容出现在其中，请和我联系：**huangailin@megvii.com / p2oileen@whu.edu.cn**。如果您希望向数据集贡献您制作的内容，也欢迎和我联系！

### 使用注意事项
1. 请尊重MMD社区工作者的劳动成果，遵循圈内协定的普遍规则。具体而言，当您使用某个动作或模型时，请务必遵循README中的原作者要求（如credit等）。如果因为不当使用导致任何问题，CoNR作者不承担任何责任。
2. MMD模型数据和动作数据不具有普遍格式，可能出现各种问题。然而，鉴于CoNR的训练只使用这些数据生成UDP和图像，不需要非常严格的动作准确性要求，我并没有做修改。如果您对这方面要求比较高，请重新筛选一遍，或者手动修一下模型。
3. 动作数据未进行仔细的清洗，有一些.vmd文件可能是相机动作文件或者各类配件的动作文件，请小心判别。

# CoNR データセット

このファイルは、OpenAIのGPT-4（ChatGPT）によって翻訳されました。

このデータセットは、GitHubプロジェクト：IJCAI2023-CoNR によって収集および生成されています。この文書は、データセットの照合手順と合意です。
元のプロジェクトのアドレス：[https://github.com/megvii-research/IJCAI2023-CoNR](https://github.com/megvii-research/IJCAI2023-CoNR)。

このデータセットは研究利用のみであり、**ダウンロードすることで私たちのルールに同意することになります**。すべてのコミュニティ著者の努力に心から感謝します。

## データのダウンロードと解凍
[**Google ドライブ ダウンロード リンク**](https://drive.google.com/drive/folders/1hadpzwt79SG8wS45_cbZKs9S5O0_nGlb?usp=share_link) からすべてのデータをダウンロードしてください。 このうち、`CoNR_Dataset_3Dmodel_only_a*`は 3D モデル データ、`CoNR_Dataset_motion_only_a*`はモーション データ、`CoNR_Dataset_annotation_only.tar.gz`は 2D 画像のアノテーション データです。

複数のボリュームを持つデータの場合、解凍する前にそれらを結合する必要があります。 例として 3D モデル データを見てみましょう。

```
cat CoNR_Dataset_3Dmodel_only_a* > model.tar.gz
tar -zxvf model.tar.gz
```

CoNR_Dataset_annotation_only.tar.gz は直接解凍するだけ

```
tar -zxvf CoNR_Dataset_annotation_only.tar.gz
```

## 2D画像アノテーション
この部分には、`annotation`フォルダの内容が含まれます。

danbooruウェブサイトからの画像のセグメンテーションアノテーションデータを提供します。著作権の安全性を維持するため、元の画像ファイルは提供しておらず、アノテーションのみを提供しています。元の画像は自分でダウンロードする必要があります。

### 元画像のダウンロード
具体的には、`annotation`フォルダ内のファイル`0a0e3ae27041b1338aba7a4af58c313f.jpg.npz`について、接頭辞`0a0e`を抽出し、`https://cdn.donmai.us/original/0a/0e/`の形式で組み立ててください。その後、ファイルの拡張子`.npz`を削除し、残りの部分とurlを連結して`https://cdn.donmai.us/original/0a/0e/0a0e3ae27041b1338aba7a4af58c313f.jpg`を取得します。これが元画像のリンクです。

### アノテーション解凍
`scripts/unzip_annotation.py`を参照してください。アノテーションの解凍についての例を提供しています。


## モーション データと 3D モデル
この部分には、`motion` フォルダと `model` フォルダの内容が含まれます。

注意してください：私たちは、すべてのMMDコミュニティプロデューサーの権利と利益を尊重し、提供されるデータセットはインターネット上の公開情報から収集されています。一部のモデル/アクションはインターネット上で流通する統合パッケージから来ているため、元のソースを特定することはできず、元のREADME情報が含まれていることも確実ではありません。それにもかかわらず、私たちは手動でREADME情報が含まれる各モデルを検証しています（リンクで与えられた仕様の条件を確認することを含む）。私たちの選別原則は次の通りです：

私たちが公開しないもの：

1. 再配布できないコンテンツ
2. 編集してから再配布できるコンテンツのみ
3. 作者に連絡して許可を得た後にのみ再配布できるコンテンツ
4. 作者に連絡して許可を得た後にのみ使用できるコンテンツ
5. 個人的に再発行できるコンテンツのみ
6. MMD関連ソフトウェアでの使用に限定されたコンテンツ
7. READMEを含むが、復号化できないコンテンツ
8. READMEがあるが、理解できないコンテンツ
9. 過度に性的なコンテンツ

私たちが公開するもの：

1. さまざまな二次投稿を許可するコンテンツ
2. READMEがないコンテンツ、またはリンク形式で与えられた規定によりアクセスできなくなったコンテンツ
3. 変更後の再配布を許可する元のモデルの作者が含まれる修正モデル。変更者は自分のREADMEを添付しません。
4. 再配布は許可されていますが、商用利用はできません
5. 再配布は許可されていますが、元のフォルダを変更することはできません
6. GNU条件の下でのオープンソースコンテンツ
7. 中国以外の地域での再配布が許可されているが、中国での再配布が制限されているコンテンツ（GitHub/GoogleDriveでのみ公開することを約束します）
8. さまざまな使用/再配布条件があるコンテンツについては、元の作者の要件に適合した使用条件の下で再配布します（例：新しいREADMEを添付、元のリンクを添付など、すべて`README_added_by_CoNR.txt`に記載されています）

著者の外国語レベルは平均的です。READMEを読む際に、再配布の遵守を判断するためにできるだけさまざまな翻訳ツールを使用していますが、READMEには複数の言語が含まれていることが多いため、一部の省略があるかもしれません。問題がある場合、心からお詫び申し上げます。タイムリーな修正を行う意思があります。MMDコミュニティの著者の方々の監督を歓迎します。

## コンテンツの追加と削除
多くのコンテンツの著者が連絡が取れなかったり、CoNRの人員が不足していたりするため、すべての著者に連絡して意志確認を行うことができず、申し訳ありません。ルートディレクトリの `motion_model_SHA256.txt` には、すべての pmx/pmd/vmd ファイルの SHA256 コード（重複を排除してソート）が含まれており、コミュニティの著者が閲覧するのに便利です。データセット内の特定のコンテンツの著者であり、そのコンテンツがデータセットに表示されることを望まない場合は、お問い合わせください：**huangailin@megvii.com / p2oileen@whu.edu.cn**。データセットに自分のコンテンツを寄稿したい場合は、お気軽にお問い合わせください！

## 使用上の注意事項
1. MMD著者の労働成果を尊重し、コミュニティで合意された一般的なルールに従ってください。具体的には、モーションやモデルを使用する際には、READMEの中で元の著者が要求する事項（クレジットなど）を必ず守ってください。CoNRの著者は、不適切な使用によって生じる問題については一切責任を負いません。
2. MMDモデルデータとアクションデータには非常に一般的なフォーマットがなく、様々な問題が発生する可能性があります。ただし、CoNRのトレーニングでは、これらのデータを使用してUDPと画像を生成するだけであり、非常に厳密なモーション精度要求は必要とされないため、修正は行っていません。この分野で高い要求がある場合は、モデルをフィルタリングするか手動で修復してください。
3. モーションデータは注意深くクリーニングされていません。一部の.vmdファイルはカメラモーションファイルやさまざまなアクセサリーのモーションファイルである可能性がありますので、注意して区別してください。
