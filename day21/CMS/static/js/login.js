// 设置错误信息鼠标点击input自动消失
$(".login-box input").focus(function () {
    $(".login-error").text("");

    }
);

// 设置验证码点击变化
$("#v-code-img").click(function () {
    this.src+="?"

});