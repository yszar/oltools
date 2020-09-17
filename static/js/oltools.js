layui.use('element', function () {
    const element = layui.element; //导航的hover效果、二级菜单等功能，需要依赖element模块

    //监听导航点击
    element.on('nav(demo)', function (elem) {
        //console.log(elem)
        layer.msg(elem.text());
    });
});

window.onload = function () {
    var show = document.getElementById("show");
    setInterval(function () {
        var time = new Date();   // 程序计时的月从0开始取值后+1
        var m = time.getMonth() + 1;
        var t = time.getFullYear() + "-" + m + "-"
            + time.getDate() + " " + ("0" + time.getHours()).slice(-2) + ":"
            + ("0" + time.getMinutes()).slice(-2) + ":" + ("0" + time.getSeconds()).slice(-2);
        show.innerHTML = t;
    }, 1000);
};

layui.use('carousel', function () {
    var carousel = layui.carousel;
    //建造实例
    carousel.render({
        elem: '#cloud-ad'
        , width: '100%' //设置容器宽度
        , height: '149px'
        , arrow: 'hover' //始终显示箭头
        , indicator: 'outside' //始终显示箭头
        //,anim: 'updown' //切换动画方式
    });
});