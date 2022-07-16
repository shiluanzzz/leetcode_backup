
    let MRRSXZ = 10000;
    function JSONLength(obj) {
        var size = 0, key;
        for (key in obj) {
        if (obj.hasOwnProperty(key)) size++;
        }
        return size;
    };
    let row_limit = 2;
    let col_limit = 1;
    let chosenNum = 0;
    var chosenPlace = '';       //选择地
    let num = [];
    let row_num = {};
    $(".canRes").click(function () {
        if ($(this).html() === '已过期' || $(this).html() === '已预定'){
            return;
        }
        let cddm = $(this).attr('cddm');
        if (row_num[cddm] === undefined){
            if (JSONLength(row_num) +1  > col_limit){
                swal("选择失败!", "单次预约最多能预约" + col_limit.toString() +"个场地", "error");
                return;
            }
            if (row_limit <= 0){
                 swal("选择失败!", "超过每日最大预约时间2小时限制", "error");
                 return
             }
            if (($(this).attr("isChosen") === "false")) {
                let total_limit = 0;
                for(let p in row_num){//遍历json数组时，这么写p为索引，0,1
                    total_limit += row_num[p].length;
                }
                if (row_limit <= 0 || total_limit >= row_limit) {
                    swal("选择失败!", "超过每日最大预约时间2小时限制", "error");
                    return
                } else {
                    row_num[cddm] = [$(this).attr('time')];
                    if (row_num[cddm].length > row_limit){
                         swal("选择失败!", "超过每日最大预约时间2小时限制", "error");
                         return
                    }
                }

            }
        }
        else {
            if (($(this).attr("isChosen") === "false")) {
                let total_limit = 0;
                for(let p in row_num){//遍历json数组时，这么写p为索引，0,1
                    total_limit += row_num[p].length;
                }
                if (row_limit <= 0 || row_num[cddm].length >= row_limit || total_limit >= row_limit) {
                    swal("选择失败!", "超过每日最大预约时间2小时限制", "error");
                    return
                } else {
                    row_num[cddm].push($(this).attr('time'));
                }
            }
        }
        if ($(this).text() === '已预定' || $(this).text() === '已过期') {}
        else {
            if ($(this).attr("isChosen") === "true") {
                $(this).attr("isChosen", "false");
                row_num[cddm].pop()
                if (row_num[cddm].length === 0){
                    delete row_num[cddm];
                }
                $(this)[0].childNodes[3].remove();
                chosenNum--;
                if (chosenNum == 0) {
                    chosenPlace = '';
                }
            } else {
                if ($("a[class='nav-link active'][style='background-color: #99CC00']").text() === '篮球场') {
                    $(this).attr("isChosen", "true");
                    if (num.includes($(this).attr('cddm'))) {
                        $(this).append('<img class="chooseImg showAnimR" src="/static/images/choose.png" alt="">');
                    } else {
                        $(this).append('<img class="chooseImg showAnimR" src="/static/images/choose.png" alt="">');
                        num.push($(this).attr('cddm'))
                    }
                }
                else {
                    $(this).append('<img class="chooseImg showAnimR" src="/static/images/choose.png" alt="">');
                    $(this).attr("isChosen", "true");
                    chosenPlace = $(this).attr("place");
                    chosenNum++;
                }
            }
        }
    })

    $('.animNav li a').click(function () {
        box = document.getElementById('animBox');
        if (box.classList.contains('playAnim')) {
            box.className = 'restart';
        } else {
            box.className = 'playAnim';
        }
    })

    //通行状态判断
    function huoquTX(YYBH) {
        $.post("/2021/08/29/book/check_ticket", {'yybh': YYBH}, function (res) {
            if (res.RTN_CODE === "00") {
                $("#TXZT").addClass('faile_credentials');
                $("#TXZTM").empty();
                $("#TXZTM").append('<div style="color: red;font-size: 16px;">' + res.RTN_MSG + '</div>');
                $("#TXZTM").append('<span class="glyphicon glyphicon-remove-circle faile_color"></span>');
            } else if (res.RTN_CODE === "01") {
                $("#TXZT").addClass('success_credentials');
                $("#TXZTM").empty();
                $("#TXZTM").append('<div style="color: forestgreen;font-size: 16px;">' + res.RTN_MSG + '</div>');
                $("#TXZTM").append('<span class="glyphicon glyphicon-upload success_color"></span>');
            }
        }).fail(function () {
            swal("获取失败", '网络错误！', "error");
        })
    }

    //预约凭证信息展示
    function credentials_information(CDLXMC, CDMC, YYRQ, YYSJD, CDBH, YYLX, YYBH) {
        $.post("/2021/08/29/book/get_txr", {'yycdbh': CDBH,'yyrq': YYRQ,'yysjd':YYSJD} , function (res){
            $("#credentials-information").empty();
            $("#TXZT").removeClass($("#TXZT").attr('class'));
            $("#TXZTM").empty();
            if (YYBH) {
                $("#TXZTM").append('<button  style="display: none" class="btn btn-info" onclick="huoquTX(' + YYBH + ')">获取通行码</button>');
            }
            if(res.DATA.length === 0) {
                $("#credentials-information").append('<div class="row" style="padding: 5px 30px;">\n' +
            '                <div style="margin: 5px 0;" class="col-xs-5">\n' +
            '                    <span>场地：</span>\n' +
            '                </div>\n' +
            '                <div style="margin: 5px 0;text-align: right;" class="col-xs-7">\n' +
            '                    <span>' + CDLXMC + ' ' + CDMC + '</span>\n' +
            '                </div>\n' +
            '                <div style="margin: 5px 0;" class="col-xs-5">\n' +
            '                    <span>日期：</span>\n' +
            '                </div>\n' +
            '                <div style="margin: 5px 0;text-align: right;" class="col-xs-7">\n' +
            '                    <span>' + YYRQ + '</span>\n' +
            '                </div>\n' +
            '                <div style="margin: 5px 0;" class="col-xs-5">\n' +
            '                    <span>时间：</span>\n' +
            '                </div>\n' +
            '                <div style="margin: 5px 0;text-align: right;" class="col-xs-7">\n' +
            '                    <span>' + YYSJD + '</span>\n' +
            '                </div>\n' +
            '                <div style="margin: 5px 0;" class="col-xs-5">\n' +
            '                    <span>预约类型：</span>\n' +
            '                </div>\n' +
            '                <div style="margin: 5px 0;text-align: right;" class="col-xs-7">\n' +
            '                    <span>' + YYLX + '</span>\n' +
            '                </div>\n' +
            '                <div style="margin: 5px 0;" class="col-xs-5">\n' +
            '                    <span>同行人：</span>\n' +
            '                </div>\n' +
            '                <div style="margin: 5px 0;text-align: right;" class="col-xs-7">\n' +
            '                    <span>无同行人管理中的人</span>\n' +
            '                </div>\n' +
            '            </div>')
            }
            else {
                $("#credentials-information").append('<div class="row" style="padding: 5px 30px;">\n' +
            '                <div style="margin: 5px 0;" class="col-xs-5">\n' +
            '                    <span>场地：</span>\n' +
            '                </div>\n' +
            '                <div style="margin: 5px 0;text-align: right;" class="col-xs-7">\n' +
            '                    <span>' + CDLXMC + ' ' + CDMC + '</span>\n' +
            '                </div>\n' +
            '                <div style="margin: 5px 0;" class="col-xs-5">\n' +
            '                    <span>日期：</span>\n' +
            '                </div>\n' +
            '                <div style="margin: 5px 0;text-align: right;" class="col-xs-7">\n' +
            '                    <span>' + YYRQ + '</span>\n' +
            '                </div>\n' +
            '                <div style="margin: 5px 0;" class="col-xs-5">\n' +
            '                    <span>时间：</span>\n' +
            '                </div>\n' +
            '                <div style="margin: 5px 0;text-align: right;" class="col-xs-7">\n' +
            '                    <span>' + YYSJD + '</span>\n' +
            '                </div>\n' +
            '                <div style="margin: 5px 0;" class="col-xs-5">\n' +
            '                    <span>预约类型：</span>\n' +
            '                </div>\n' +
            '                <div style="margin: 5px 0;text-align: right;" class="col-xs-7">\n' +
            '                    <span>' + YYLX + '</span>\n' +
            '                </div>\n' +
            '                <div style="margin: 5px 0;" class="col-xs-5">\n' +
            '                    <span>同行人：</span>\n' +
            '                </div>\n' +
            '                <div style="margin: 5px 0;text-align: right;" class="col-xs-7">\n' +
            '                    <span>' + res.DATA[0].TXRXM + '</span>\n' +
            '                </div>\n' +
            '            </div>')
            }
        })
    }

    //最后提交
    function end_submit() {
        let txrsfrzhArray = new Array();
        for (let i = 0; i < $("tr[class='selected']").length; i++) {
            txrsfrzhArray.push($($("tr[class='selected']")[i])[0].cells[1].innerText)
        }
        let yycdbhArray = new Array();
        let yyrq = $("a[class*='active'][href='javascript:']")[0].children[0].innerText

        for (let i = 0; i < $("li[ischosen='true']").length; i++) {
            if (!yycdbhArray.includes($($("li[ischosen='true']")[i]).attr('cddm'))) {
                yycdbhArray.push($($("li[ischosen='true']")[i]).attr('cddm'))
            }
        }
        for (let i = 0; i < yycdbhArray.length; i++) {
            let txrsfrzh = new Array();
            for (let I = i; I < txrsfrzhArray.length;) {
                txrsfrzh.push(txrsfrzhArray[I]);
                I += yycdbhArray.length
            }
            for (let timenum = 0; timenum < $("li[ischosen='true'][cddm = " + yycdbhArray[i] + "]").length; timenum++) {
                let yydsj = $($("li[ischosen='true'][cddm = " + yycdbhArray[i] + "]")[timenum]).attr("time");
                let yycdbh = yycdbhArray[i];
                $.post("/2021/08/29/book/book", {
                    "txrsfrzh": "" + txrsfrzh,
                    "yysj": yydsj.replace('(', ''),
                    "yyrq": yyrq,
                    "yycdbh": yycdbh,
                }, function (res) {
                    if (res.RTN_CODE === "00") {
                        $("div.modal-backdrop.fade.in").remove();
                        $("div.modal-backdrop.fade.show").remove();
                        swal("预约失败", res.RTN_MSG, "error");
                    } else {
                        swal("预约成功", res.RTN_MSG, "success");
                        setTimeout(function () {
                            location.reload();
                        }, 1000);
                        return;
                    }
                }).fail(function () {
                    swal("预约失败", '网络错误！', "error");
                })
            }
        }
    }

    //提交处理
    function addFriendModal() {
        $("#box_clearance").show()
        $("#head_submit").hide()
        $("#head_add").show()
        $("#end_submit").hide()
        $("#box_clearance").show()
    }

    function submit() {
        let yycdbh, yydsj;
        let yyrq = $("a[class*='active'][href='javascript:']")[0].children[0].innerText
        if($("li[ischosen='true']").length === 0){
            swal("锁定失败","未选择场地", "error");
        }
        else {
            $("#addFriendModal").modal("show");
            for (let i = 0; i < $("li[ischosen='true']").length; i++) {
                yycdbh = $($("li[ischosen='true']")[i]).attr("cddm");
                yydsj = ($($("li[ischosen='true']")[i]).attr("time"));
                $.post("/2021/08/29/book/check_playground_status", {
                    "yysjd": yydsj,
                    "yyrq": yyrq,
                    "yycdbh": yycdbh,
                }, function (res) {
                    if (res.RTN_CODE === "00") {
                        $("div.modal-backdrop.fade.in").remove();
                        $("div.modal-backdrop.fade.show").remove();
                        swal("锁定失败", res.RTN_MSG, "error");
                        return;
                    } else {
                        swal("锁定成功", res.RTN_MSG, "success");
                    }
                }).fail(function () {
                swal("预约失败", '网络错误！', "error");
            })
        }
        $("#box_clearance").hide()
        $("#head_submit").show()
        $("#head_add").hide()
        $("#box_clearance").hide()
        $("#end_submit").show()
        }
    }

    //记录管理
    function make_appointment(e) {
        if (e === '00') {
            $("#make_appointment00").removeClass($("#make_appointment00").attr('class'));
            $("#make_appointment01").removeClass($("#make_appointment01").attr('class'));
            $("#make_appointment00").addClass('btn btn-warning');
            $("#make_appointment01").addClass('btn btn-modal');
            $("#find_friendsTable").bootstrapTable('destroy');
            $('#find_friendsTable').bootstrapTable({
                url: '/2021/08/29/book/book_history',
                method: 'get', // 请求方式（*）
                dataType: "json", // 返回格式（*）
                clickToSelect: true, //是否启用点击选中行
                columns: [{
                    field: 'CDBH',
                    title: '场地编号',
                    visible: false,
                }, {
                    field: 'TXR',
                    title: '同行人',
                    visible: false,
                }, {
                    field: 'YYLX',
                    title: '预约类型',
                    visible: false,
                }, {
                    field: 'YYBH',
                    title: '预约编号',
                    visible: false,
                }, {
                    field: 'YYRQ',
                    title: '预约日期',
                    visible: false,
                }, {
                    align: 'center',
                    valign: 'middle',
                    field: 'CDLXMC',
                    title: '类型',
                }, {
                    align: 'center',
                    valign: 'middle',
                    field: 'CDMC',
                    title: '场地',
                }, {
                    align: 'center',
                    valign: 'middle',
                    field: 'ZSRQ',
                    title: '预约日期',
                }, {
                    align: 'center',
                    valign: 'middle',
                    field: 'YYSJD',
                    title: '时间',
                }, {
                    align: 'center',
                    title: '状态',
                    formatter: function (value, Data, index) {
                        if (Data.ZT === '时间未到') {
                            return '<div><i style="color: red;" class="glyphicon glyphicon-time"></i></div>'
                        } else if (Data.ZT === '运动中') {
                            return '<div><i style="color: forestgreen;" class="glyphicon glyphicon-arrow-up"></i></div>'
                        }
                    }
                }, {
                    title: '操作',
                    align: 'center',
                    width: '80px',
                    formatter: function (value, row, index) {
                        data = '<span data-toggle="modal" onclick="credentials_information(\'' + row.CDLXMC + '\',\'' + row.CDMC + '\',\'' + row.YYRQ + '\',\'' + row.YYSJD + '\',\'' + row.CDBH + '\',\'' + row.YYLX + '\',\'' + row.YYBH + '\')" data-target="#credentials" style="margin-right: 10px;"><i class="glyphicon glyphicon-list-alt"></i></span>'
                        if(row.YYLX === "自约") {
                            data += '<span onclick="delete_appointment(' + row.CDBH + ',\'' + row.YYRQ + '\',\'' + row.YYSJD + '\')"style="margin-left: 10px;"><i class="glyphicon glyphicon-trash"></i></span>'
                        }
                        return data;
                    }
                }],
                responseHandler: function (res) {
                    console.log(res)
                    let Data = [];
                    for (let i in res.DATA[0]) {
                        let now_time = new Date().getTime();
                        timestare = timeZh(res.DATA[0][i].YYRQ + ' ' + res.DATA[0][i].YYSJD.split('-')[0]);
                        timeend = timeZh(res.DATA[0][i].YYRQ + ' ' + res.DATA[0][i].YYSJD.split('-')[1]);
                        if (now_time < timestare) {
                            res.DATA[0][i].ZSRQ = res.DATA[0][i].YYRQ.split("-")[1]+"-"+res.DATA[0][i].YYRQ.split("-")[2];
                            res.DATA[0][i].ZT = "时间未到";
                            Data.push(res.DATA[0][i])
                        } else if (timeend <= now_time) {
                            continue
                        } else {
                            res.DATA[0][i].ZSRQ = res.DATA[0][i].YYRQ.split("-")[1]+"-"+res.DATA[0][i].YYRQ.split("-")[2];
                            res.DATA[0][i].ZT = "运动中";
                            Data.push(res.DATA[0][i])
                        }
                    }

                    function timeZh(time) {
                        date = time.substring(0, 19);
                        date = date.replace(/-/g, '/');
                        var timestamp = new Date(date).getTime();
                        return timestamp;
                    }

                    return Data;
                },
            })
        } else if (e === '01') {
            $("#make_appointment01").removeClass($("#make_appointment01").attr('class'));
            $("#make_appointment00").removeClass($("#make_appointment00").attr('class'));
            $("#make_appointment01").addClass('btn btn-warning');
            $("#make_appointment00").addClass('btn btn-modal');
            $("#find_friendsTable").bootstrapTable('destroy');
            $('#find_friendsTable').bootstrapTable({
                url: '/2021/08/29/book/book_history',
                method: 'get', // 请求方式（*）
                dataType: "json", // 返回格式（*）
                clickToSelect: true, //是否启用点击选中行
                columns: [{
                    field: 'CDBH',
                    title: '场地编号',
                    visible: false,
                }, {
                    field: 'TXR',
                    title: '同行人',
                    visible: false,
                }, {
                    field: 'YYLX',
                    title: '预约类型',
                    visible: false,
                }, {
                    align: 'center',
                    valign: 'middle',
                    field: 'CDLXMC',
                    title: '类型',
                }, {
                    align: 'center',
                    valign: 'middle',
                    field: 'CDMC',
                    title: '场地',
                }, {
                    align: 'center',
                    valign: 'middle',
                    field: 'YYRQ',
                    title: '预约日期',
                }, {
                    align: 'center',
                    valign: 'middle',
                    field: 'YYSJD',
                    title: '时间',
                }, {
                    align: 'center',
                    title: '状态',
                    formatter: function (value, row, index) {
                        return '<button data-toggle="modal" data-target="#credentials" onclick="credentials_information(\'' + row.CDLXMC + '\',\'' + row.CDMC + '\',\'' + row.YYRQ + '\',\'' + row.YYSJD + '\',\'' + row.CDBH + '\',\'' + row.YYLX + '\')" delId=' + row.TXRSFRZH + ' style="margin-left: 5px;" class="btn btn btn-info btn-sm D_Button" type="button">查看</button>'
                    }
                }],
                responseHandler: function (res) {
                    let timeoutData = [];
                    for (let i in res.DATA[0]) {
                        let now_time = new Date().getTime();
                        timestare = timeZh(res.DATA[0][i].YYRQ + ' ' + res.DATA[0][i].YYSJD.split('-')[0]);
                        timeend = timeZh(res.DATA[0][i].YYRQ + ' ' + res.DATA[0][i].YYSJD.split('-')[1]);
                        if (now_time < timestare) {
                            continue
                        } else if (timeend <= now_time) {
                            timeoutData.push(res.DATA[0][i])
                        } else {
                            continue
                        }
                    }

                    function timeZh(time) {
                        date = time.substring(0, 19);
                        date = date.replace(/-/g, '/');
                        var timestamp = new Date(date).getTime();
                        return timestamp;
                    }

                    return timeoutData;
                },
            })
        }
    }

    //第一次记录
    $('#find_friendsTable').bootstrapTable({
        url: '/2021/08/29/book/book_history',
        method: 'get', // 请求方式（*）
        dataType: "json", // 返回格式（*）
        clickToSelect: true, //是否启用点击选中行
        columns: [{
            field: 'CDBH',
            title: '场地编号',
            visible: false,
        }, {
            field: 'TXR',
            title: '同行人',
            visible: false,
        }, {
            field: 'YYLX',
            title: '预约类型',
            visible: false,
        }, {
            field: 'YYRQ',
            title: '预约日期',
            visible: false,
        }, {
            field: 'YYBH',
            title: '预约编号',
            visible: false,
        }, {
            align: 'center',
            valign: 'middle',
            field: 'CDLXMC',
            title: '类型',
        }, {
            align: 'center',
            valign: 'middle',
            field: 'CDMC',
            title: '场地',
        }, {
            align: 'center',
            valign: 'middle',
            field: 'ZSRQ',
            title: '预约日期',
        }, {
            align: 'center',
            valign: 'middle',
            field: 'YYSJD',
            title: '时间',
        }, {
            align: 'center',
            title: '状态',
            formatter: function (value, Data, index) {
                if (Data.ZT === '时间未到') {
                    return '<div><i style="color: red;" class="glyphicon glyphicon-time"></i></div>'
                } else if (Data.ZT === '运动中') {
                    return '<div><i style="color: forestgreen;" class="glyphicon glyphicon-arrow-up"></i></div>'
                }
            }
        }, {
            title: '操作',
            align: 'center',
            width: '80px',
            formatter: function (value, row, index) {
                data = '<span data-toggle="modal" onclick="credentials_information(\'' + row.CDLXMC + '\',\'' + row.CDMC + '\',\'' + row.YYRQ + '\',\'' + row.YYSJD + '\',\'' + row.CDBH + '\',\'' + row.YYLX + '\',\'' + row.YYBH + '\')" data-target="#credentials" style="margin-right: 10px;"><i class="glyphicon glyphicon-list-alt"></i></span>'
                if (row.YYLX === "自约") {
                    data += '<span onclick="delete_appointment(' + row.CDBH + ',\'' + row.YYRQ + '\',\'' + row.YYSJD + '\')"style="margin-left: 10px;"><i class="glyphicon glyphicon-trash"></i></span>'
                }
                return data;
            }
        }],
        responseHandler: function (res) {
            let Data = [];
            for (let i in res.DATA[0]) {
                let now_time = new Date().getTime();
                timestare = timeZh(res.DATA[0][i].YYRQ + ' ' + res.DATA[0][i].YYSJD.split('-')[0]);
                timeend = timeZh(res.DATA[0][i].YYRQ + ' ' + res.DATA[0][i].YYSJD.split('-')[1]);
                if (now_time < timestare) {
                    res.DATA[0][i].ZSRQ = res.DATA[0][i].YYRQ.split("-")[1]+"-"+res.DATA[0][i].YYRQ.split("-")[2];
                    res.DATA[0][i].ZT = "时间未到";
                    Data.push(res.DATA[0][i])
                } else if (timeend <= now_time) {
                    continue
                } else {
                    res.DATA[0][i].ZSRQ = res.DATA[0][i].YYRQ.split("-")[1]+"-"+res.DATA[0][i].YYRQ.split("-")[2];
                    res.DATA[0][i].ZT = "运动中";
                    Data.push(res.DATA[0][i])
                }
            }

            function timeZh(time) {
                date = time.substring(0, 19);
                date = date.replace(/-/g, '/');
                var timestamp = new Date(date).getTime();
                return timestamp;
            }

            return Data;
        },
    })

    //取消预约请求
    function delete_appointment(cdbh, yyrq, yysjd) {
        swal({
        title: "是否取消预约",
        text: "",
        type: "warning",
        showCancelButton: true,//是否显示取消按钮
        cancelButtonText: '取 消',//按钮内容
        cancelButtonColor: '#b9b9b9',
        showConfirmButton: true,
        confirmButtonText: '确 认',
        confirmButtonColor: "#dd6b55",
        closeOnConfirm: false,//点击返回上一步操作
        closeOnCancel: true
        }, function () {
            $.post('/2021/08/29/book/cancel_book', {'yycdbh': cdbh, 'yysj': yysjd, 'yyrq': yyrq}, function (res) {
                if (res.RTN_CODE === "00") {
                    swal("取消失败", res.RTN_MSG, "error");
                    return;
                } else {
                    swal("取消成功", '', "success");
                    location.reload();
                }
                updata('cdyy');
            })
        })
    }

    //同行人管理
    $('#friendsTable').bootstrapTable({
        url: '/2021/08/29/book/partner',
        method: 'get', // 请求方式（*）
        dataType: "json", // 返回格式（*）
        clickToSelect: true, //是否启用点击选中行
        columns: [{
            checkbox: true,
        }, {
            align: 'center',
            valign: 'middle',
            field: 'TXRSFRZH',
            title: '学号',
        }, {
            align: 'center',
            valign: 'middle',
            field: 'TXRXM',
            title: '姓名',
        },],
        responseHandler: function (res) {
            return res.DATA;
        },
    })

    $('#friendsTableManagement').bootstrapTable({
        url: '/2021/08/29/book/partner',
        method: 'get', // 请求方式（*）
        dataType: "json", // 返回格式（*）
        idField: 'id',
        clickToSelect: true, //是否启用点击选中行
        columns: [{
            align: 'center',
            valign: 'middle',
            field: 'TXRSFRZH',
            title: '学号',
        }, {
            align: 'center',
            valign: 'middle',
            field: 'TXRXM',
            title: '姓名',
        }, {
            field: 'operator',
            title: '操作',
            align: 'center',
            valign: 'middle',
            // visible: false,
            formatter: function (value, row, index) {
                return '<button onclick="del_txr(\'' + row.TXRSFRZH + '\')" delId=' + row.TXRSFRZH + ' style="margin-left: 5px;" class="btn btn btn-danger btn-sm D_Button" type="button">删除</button>'
            },
        }],
        responseHandler: function (res) {
            return res.DATA;
        }
    })

    function del_txr(txrsfrzh) {
        swal({
            title: "是否删除",
            text: "",
            type: "warning",
            showCancelButton: true,//是否显示取消按钮
            cancelButtonText: '取 消',//按钮内容
            cancelButtonColor: '#b9b9b9',

            showConfirmButton: true,
            confirmButtonText: '确 认',
            confirmButtonColor: "#dd6b55",

            closeOnConfirm: false,//点击返回上一步操作
            closeOnCancel: true
        }, function () {
            $.post('/2021/08/29/book/delpartner', {"sfrzh": txrsfrzh}, function (res) {
                if (res.RTN_CODE === "00") {
                    swal("删除同行人失败", res.RTN_MSG, "error");
                    return;
                } else {
                    swal("删除成功", "删除同行人成功", "success");
                    setTimeout(function () {
                        $('#friendsTableManagement').bootstrapTable('refresh');
                        $('#friendsTable').bootstrapTable('refresh');
                    }, 400);
                }
                updata('txrgl')
            })
        })
    }

    function openFriendMangement() {
        $('#addFriendModal').modal('hide');
        setTimeout(function () {
            $('#mangeFriendModal').modal('show');
        }, 400);
        $("div.modal-backdrop.fade.in").remove();
    }

    function backToFriend() {
        $('#mangeFriendModal').modal('hide');
        setTimeout(function () {
            $('#addFriendModal').modal('show');

        }, 400);
    }

    function newFriend() {
        $('#mangeFriendModal').modal('hide');
        setTimeout(function () {
            $('#addModal').modal('show');
        }, 400);
    }

    function backToFriendMangement() {
        $('#addModal').modal('hide');
        setTimeout(function () {
            $('#mangeFriendModal').modal('show');
        }, 400);
    }

    // $("#mangeFriendModal").on("hide.bs.modal", function(){
    //     $("#addFriendModal").modal('show');
    // });
    // $("#addModal").on("hide.bs.modal", function(){
    //     $("#mangeFriendModal").modal('show');
    // });

    function add_partner() {
        $.post("/2021/08/29/book/addpartner", {
            "sfrzh": $("#partner_sfrzh").val(),
            "xm": $("#partner_xm").val()
        }, function (res) {
            if (res.RTN_CODE === "00") {
                swal("新增同行人失败", res.RTN_MSG, "error");
                return;
            } else {
                swal("新增成功", res.RTN_MSG, "success");
                    $("#partner_sfrzh").val('');
                    $("#partner_xm").val('');
                setTimeout(function() {
                    $('#friendsTableManagement').bootstrapTable('refresh');
                    $('#friendsTable').bootstrapTable('refresh');
                    // $('#addModal').modal('hide');
                    },1000)
                // setTimeout(function () {
                //     $('#mangeFriendModal').modal('show');
                // }, 400);
            }
        })
    }

    //列表更改渲染
    function updata(e) {
        if (e === 'cdyy') {
            let opt = {
                url: '/2021/08/29/book/book_history',
            }
            $("#find_friendsTable").bootstrapTable('refreshOptions', opt);
        } else if (e === 'txrgl') {
            let opt = {
                url: '/2021/08/29/book/partner',
            }
            $("#friendsTable").bootstrapTable('refreshOptions', opt);
        }
    }

    function change_date(choose_date) {
        window.location.href = '/2021/08/29/book?cdmc=羽毛球&date=' + choose_date;
    }

    $(function () {
        let weekDay = ["星期天", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"];
        let yyrq = $("*[name='YYRQ']");
        let yyrq_xq = $("*[name='YYRQ_XQ']");
        for (let i = 0; i < yyrq.length; i++){
            yyrq_xq[i].innerHTML =  weekDay[new Date(Date.parse(yyrq[i].innerHTML.replace(/-/g, "/"))).getDay()];
        }
    })