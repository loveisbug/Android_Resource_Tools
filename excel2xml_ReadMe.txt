excel2xml.exe工具可以生成Android项目中使用的strings.xml文件。

在excel文件中（文件名必须是translation_table.xls，第一个标签页必须是string list页面）：
    第一列是Android项目中使用的string id。
    [第二列]是项目筛选列，筛选后隐藏该列。
    [第三列]是描述列，详细描述该string使用场景。
    从第四列开始是多语言翻译。
    未翻译的string默认使用英语填写。
    第一行是标题行。

在命令行窗口运行excel2xml.exe:
    需要3个命令行参数，第1个是项目路径，相对于当前路径的相对路径；第2个是设备名；第3个是App名。
    譬如：excel2xml ..\..\..\svncpy\ant\trunk\Android\TVman_DVB TVman TVman DVB。
    程序会在同目录下寻找translation_table.xls。
    程序会生成若干个名字为strings_xxx.xml的xml文件，xxx是语种（excel文件中的第一行）。

-------------- Release Notes -----------------------------------------------------------
2014-08-04
  - V0.4.1
  - support 3 parameters, copy strings.xml to the project path.

2013-06-14
  - V0.3.0
  - support 2 parameters, device name and App name.

2013-06-08
  - V0.2.0
  - use xlrd instead of pyExcelerator.

2012-08-17
  - V0.1.3
  - "\'" instead of "'" for strings.xml in values-fr-rFR(franch language).

2012-07-06
  - V0.1.2
  - remove no-used variable, add error print info.

2012-06-05
  - V0.1.1
  - support get app name from command line arguments.

2012-05-29
  - V0.0.2
  - generate strings.xml from xls file.