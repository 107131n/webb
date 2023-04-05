    // 한 줄 주석
    /*
        문단 단위 주석
    */
        function alertView(){
            alert('알림창 띄우기');
        }

        // css1으로 가기
        function goCss1(){
            alert("goCss1() 함수가 호출되었습니다.");
            location.href = "/front/css_1/";
        }

        // css2으로 가기
        function goCss2(){
            alert("goCss2() 함수가 호출되었습니다.");            
            location.href = "/front/css_2/";
        }

        // css3으로 가기
        function goCss3(){
            alert("goCss3() 함수가 호출되었습니다.");
            location.href = "/front/css_3/";
        }

        // 통합 함수
        function goCss(no){
        alert("goCss() 함수가 호출되었습니다. js");
        location.href = "/front/css_"+no+"/";
        }