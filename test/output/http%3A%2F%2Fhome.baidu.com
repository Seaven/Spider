<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312">
<title>关于百度</title>
<link href="http://home.baidu.com/resource/r/home/style.css" rel="stylesheet" type="text/css">
<script language="javascript" src="http://home.baidu.com/resource/r/home/menu.js"></script>
<script src="http://home.baidu.com/resource/r/home/flash.js" language="javascript"></script>
</head>

<body>
<!--顶部开始 --><div id="head"><a href="http://www.baidu.com/"><img src="http://home.baidu.com/resource/r/home/img/logo-yy.gif" class="log"></a></div><!--顶部结束 -->
<table border="0" cellspacing="0" cellpadding="0" id="menu">
  <tr>
    <td><!--顶部导航开始 --><script language="javascript">menuTop(1);</script><noscript>如果您关闭了浏览器的javascript，可能导致页面部分功能无法显示，请开启javascript以便正常浏览本网页。</noscript><!--顶部导航结束 -->
</td>
    <td width="240"><!--站内搜索开始 --><script>
			function doSearch(form){
				form.ct.value = "2097152";
				form.si.value = "home.baidu.com";
				form.tn.value = "baidulocal";
				form.action = "http://www.baidu.com/s";
				return true;
			}
function cls(tar){
    if(tar.value==tar.getAttribute('defaultvalue')) tar.value="";
}
function res(tar){
    if(tar.value=='') tar.value=tar.getAttribute('defaultvalue');
}
			document.write("<FORM name=f1 onsubmit='return doSearch(this);'>");
			document.write("<INPUT type=hidden name=tn><INPUT type=hidden name=si><INPUT type=hidden name=ct>");
			document.write("<INPUT class=formfont size=16 name=word style='border:1px solid #7f9db9;background:url(http://home.baidu.com/resource/r/home/img/dot6.gif) no-repeat;padding-left:28px;color: #cbcbcb' onfocus='cls(this);' onblur='res(this);' value=\"站内搜索\"  defaultvalue=\"站内搜索\" onClick= \"javascript:if(this.value=='站内搜索')this.value=''\";>&nbsp;");
			document.write("<INPUT type=submit value=百度一下>");
		</script><!--站内搜索结束 -->
</td>
  </tr>
</table>
<!--页面banner开始 -->
<div class="bnrInd">
  <script language="javascript">
	//初始化Flash时，包含xml路径
	CreateFlash("banner", "http://home.baidu.com/resource/r/home/banner.swf", 1002, 280, "data=http://home.baidu.com/inddata.xml");
</script></div>
<!--页面banner结束 -->

<div id="main">
  <div class="indLeft1"><span class="f14b">新闻动态</span>
    <ul class="indLsit1">
       
<li><strong>12/23/2015</strong><br>
<a href="http://home.baidu.com/2016-01-05/1452770885.html" target="_blank">携手国金证券 百度拿下互联网金融“三板...</a></li>
       
<li><strong>12/23/2015</strong><br>
<a href="http://home.baidu.com/2016-01-05/1453308209.html" target="_blank">百度与北京协和医学院合作开展食管癌研究...</a></li>
       
<li><strong>12/18/2015</strong><br>
<a href="http://home.baidu.com/2016-01-05/1455836314.html" target="_blank">习近平三问无人车 李彦宏乌镇刮起技术风</a></li>
       
<li><strong>12/11/2015</strong><br>
<a href="http://home.baidu.com/2016-01-05/1457061062.html" target="_blank">2015中国文化产业峰会在西安举办 李彦宏...</a></li>
       
<li><strong>12/08/2015</strong><br>
<a href="http://home.baidu.com/2016-01-05/1461433792.html" target="_blank">李彦宏出席“2015中国企业领袖年会”</a></li>
       
<li><strong>12/03/2015</strong><br>
<a href="http://home.baidu.com/2016-01-05/1459905192.html" target="_blank">百度携手亚马逊中国升级数字阅读与视听体...</a></li>
            <li><a href="http://home.baidu.com/news/news/">更多&raquo;</a></li>
    </ul>

  </div>
  
  <div class="indLeft2">
   <span class="f14b">百度直达</span>
   <ul class="indLsit2">
        <li>帮助中心
  <table width="100%" border="0" cellspacing="0" cellpadding="0">
      <tr>
         <td><a href="http://www.baidu.com/search/page_feature.html" target="_blank">搜索特色>></a></td>
         <td><a href="http://www.baidu.com/search/skill.html" target="_blank">搜索技巧>></a></td>
         <td><a href="http://www.baidu.com/search/zhinan.html" target="_blank">新手指南>></a></td>
       </tr>
   </table>
</li>
        <li>用户联系
  <table width="100%" border="0" cellspacing="0" cellpadding="0">
      <tr>
         <td><a href="http://home.baidu.com/contact.html" target="_blank">联系方式>></a></td>
         <td><a href="http://home.baidu.com/contact/visitbaidu.html" target="_blank">参观百度>></a></td>
         <td><a href="http://tousu.baidu.com/" target="_blank">投诉中心>></a></td>
       </tr>
   </table>
</li>
        <li>招聘信息
  <table width="100%" border="0" cellspacing="0" cellpadding="0">
      <tr>
         <td><a href="http://hr.baidu.com/" target="_blank">社会招聘>></a></td>
         <td><a href="http://tongxue.baidu.com/" target="_blank">校园招聘>></a></td>
         <td><a href="http://shixisheng.baidu.com/" target="_blank">实习生招聘>></a></td>
       </tr>
   </table>
</li>
        <li>百度推广
  <table width="100%" border="0" cellspacing="0" cellpadding="0">
      <tr>
         <td><a href="http://e.baidu.com/client/" target="_blank">成功故事>></a></td>
         <td><a href="http://e.baidu.com/product/" target="_blank">产品介绍>></a></td>
         <td><a href="http://e.baidu.com/faq/" target="_blank">常见问题>></a></td>
       </tr>
   </table>
</li>
        <li>品牌营销
  <table width="100%" border="0" cellspacing="0" cellpadding="0">
      <tr>
         <td><a href="http://brandlink.baidu.com/index.php" target="_blank">品牌专区>></a></td>
         <td><a href="http://ad.baidu.com/fuwu_1_5.html" target="_blank">精准广告>></a></td>
         <td><a href="http://ad.baidu.com/fuwu_1_4.html" target="_blank">社区营销>></a></td>
       </tr>
   </table>
</li>
        <li>百度联盟
  <table width="100%" border="0" cellspacing="0" cellpadding="0">
      <tr>
         <td><a href="http://union.baidu.com" target="_blank">关于联盟>></a></td>
         <td><a href="http://union.baidu.com/product/prod-cpro.html" target="_blank">业务合作>></a></td>
         <td><a href="http://yingxiao.baidu.com/support/union/?controller=index&action=main&castk=LTE%3D" target="_blank">支持中心>></a></td>
       </tr>
   </table>
</li>
        <li>百度校园
  <table width="100%" border="0" cellspacing="0" cellpadding="0">
      <tr>
         <td><a href="http://campus.baidu.com/activity" target="_blank">校园活动>></a></td>
         <td><a href="http://campus.baidu.com/course" target="_blank">校园课程>></a></td>
         <td><a href="http://campus.baidu.com/pages/about" target="_blank">校园联系>></a></td>
       </tr>
   </table>
</li>
   </ul>
    
  </div>
  <div class="indRight">
       <ul class="indLsit3">
        <li>
          <table width="100%" border="0" cellspacing="0" cellpadding="0">
            <tr>
              <td width="105"><img src="http://home.baidu.com/resource/r/image/2014-11-27/cded7324a878249049285f27093fb1db.jpg"></td>
<td><a href="http://logo.baidu.com/" target="_blank" class="f14">百度趣画正式上线 </a><br>
               欣赏百度节日logo，为你喜欢的创意点赞，请进入百度趣画！ </td>
            </tr>
          </table>
        </li>     <li>
          <table width="100%" border="0" cellspacing="0" cellpadding="0">
            <tr>
              <td width="105"><img src="http://home.baidu.com/resource/r/image/2012-12-11/33fc59dbb24ce61c883227031d958ba9.jpg"></td>
<td><a href="http://edu.baidu.com/" target="_blank" class="f14">百度营销大学</a><br>
               百度营销大学以“让营销人都懂互联网营销”为使命，致力于推动中国营销人员互联网营销水平的不断提升！</td>
            </tr>
          </table>
        </li>
        <li>
          <table width="100%" border="0" cellspacing="0" cellpadding="0">
            <tr>
              <td width="105"><img src="http://home.baidu.com/resource/r/image/2011-05-10/1467988a3a3e68edeb6ed07b33207f7f.jpg"></td>
<td><a href="http://gongyi.baidu.com/" target="_blank" class="f14">弥合信息鸿沟 共享知识社会</a><br>
               百度公益频道全新上线，致力于集合百度人民和四亿网民的力量打造全球最大的公益信息平台！ </td>
            </tr>
          </table>
        </li>
      <li>
          <table width="100%" border="0" cellspacing="0" cellpadding="0">
            <tr>
              <td width="105"><img src="http://home.baidu.com/resource/r/image/2009-12-21/fd0b8c296e71ec60dbf899c06f8da3bb.gif"></td>
<td><a href="http://campus.baidu.com/" target="_blank" class="f14">百度校园正式上线
</a><br>
               百度校园倾听来自校园的声音，展开与校园师生的互动，是百度与学校沟通的桥梁</td>
            </tr>
          </table>
        </li>
    </ul>
    </div>
  <div class="clear"></div>
</div><!--页脚其他链接开始 --><div id="pgft"><div>
<a href="http://gongyi.baidu.com/" target="_blank">百度公益</a>&nbsp;&nbsp;|&nbsp;&nbsp;
<a href="http://csr.baidu.com/" target="_blank">社会责任</a>&nbsp;&nbsp;|&nbsp;&nbsp;
<a href="http://ir.baidu.com/" target="_blank">About Baidu</a>
</div></div><!--页脚其他链接结束 -->
<!--页脚版权信息开始 --><div id="ft">&copy;2014 Baidu <a href="http://www.baidu.com/duty/">使用百度前必读</a> <a href="http://www.miibeian.gov.cn" target="_blank">京ICP证030173号</a> <img src="http://gimg.baidu.com/img/gs.gif"></div>
<!--页脚版权信息结束 -->
<script type="text/javascript">
var _bdhmProtocol = (("https:" == document.location.protocol) ? " https://" : " http://");
document.write(unescape("%3Cscript src='" + _bdhmProtocol + "hm.baidu.com/h.js%3Fb9a77820b2fa17d7223b50a01ab1aa7a' type='text/javascript'%3E%3C/script%3E"));
</script>
</body>
</html>