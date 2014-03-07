function lexical_search()
{
  document.getElementById("sentence_div").innerHTML=""
  document.getElementById("lemma_div").innerHTML=""
var xmlhttp;
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
    document.getElementById("sentence_div").innerHTML=xmlhttp.responseText;
    }
  }
xmlhttp.open("GET","http://0.0.0.0:9000/lexical_search/"+
  "?query="+document.getElementById("QueryBox").value+
  "#author="+document.getElementById("AuthorBox").value+
  "#fromyear="+document.getElementById("FromYearBox").value+
  "#tillyear="+document.getElementById("TillYearBox").value
  ,true);
xmlhttp.send();
}

function no_refresh_lexsearch(queryword)
{
  
var xmlhttp;
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
    document.getElementById("sentence_div").innerHTML= xmlhttp.responseText;
    
    }
  }

xmlhttp.open("GET","http://0.0.0.0:9000/lexical_search/"+
  "?query="+queryword+
  "#author="+document.getElementById("AuthorBox").value+
  "#fromyear="+document.getElementById("FromYearBox").value+
  "#tillyear="+document.getElementById("TillYearBox").value
  ,true);

xmlhttp.send();
}

function lemma_search()
{
  document.getElementById("sentence_div").innerHTML=""
  document.getElementById("lemma_div").innerHTML=""
var xmlhttp;
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
    document.getElementById("lemma_div").innerHTML=xmlhttp.responseText;
    }
  }
xmlhttp.open("GET","http://0.0.0.0:9000/lemma_search/"+
  "?query="+document.getElementById("QueryBox").value+
  "#author="+document.getElementById("AuthorBox").value+
  "#fromyear="+document.getElementById("FromYearBox").value+
  "#tillyear="+document.getElementById("TillYearBox").value
  ,true);
xmlhttp.send();
}