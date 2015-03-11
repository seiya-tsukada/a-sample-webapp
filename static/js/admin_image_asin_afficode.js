$(document).ready(function(){
  $(function(){
    // 登録
    $("#register-button").click(
      function(){
        var tr = $("table tr");

        for(var i=0, l=tr.length; i<l; i++){
          var cells = tr.eq(i).children();
          var api_ret = "";
          var post_param = {
            asin :  "",
            affiliate_code_url : ""
          };

          if(cells.eq(3).is("td") && cells.eq(4).is("td") && cells.eq(4).children().val()){
            post_param["asin"] = cells.eq(3).text();
            post_param["affiliate_code_url"] = cells.eq(4).children().val();
          
            post_ajax(post_param);

          }
        }
      }
    );

    // 削除
    $(".image-delete-button").click(
      function(){
        var post_param = {
          asin : $(this).attr("asin")
        }
        
        delete_ajax(post_param);
      }
    );

  });
});

function post_ajax(post_param){
  $.ajax({
    url : "/api/afficode_register/",
    type : "POST",
    dataType: "json",
    data : JSON.stringify(post_param),
    contentType: "application/json",
    success: function(data) {
      if (data["return"] == "OK") {
        return
      }
    },
    error: function(XMLHttpRequest, textStatus, errorThrown) {
      alert("NG");
    }
  });
}

function delete_ajax(post_param){
  $.ajax({
    url : "/api/afficode_delete/",
    type : "POST",
    dataType: "json",
    data : JSON.stringify(post_param),
    contentType: "application/json",
    success: function(data) {
      if (data["return"] == "OK") {
        location.reload();
      }
    },
    error: function(XMLHttpRequest, textStatus, errorThrown) {
      alert("NG");
    }
  });
}
