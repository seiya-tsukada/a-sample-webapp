$(document).ready(function(){
  $("#allCheck").on("click", function() {
    $("input[name=image_asin]").prop("checked", this.checked);
  });
});
