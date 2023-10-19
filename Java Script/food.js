let d=document.createElement("div")

let img1=document.createElement("img")
img1.src="	https://www.foodfood.com/assets/images/logo/logo.png"


let d1=document.createElement("div")
d1.setAttribute("id","abc")

let p=document.createElement("table")
p.innerHTML="HOME"
p.setAttribute("id","b")
p.setAttribute("id","ab")



    let s=document.createElement("select");
    let op=document.createElement("option")
    op.innerHTML="CHEFS"
    s.setAttribute("id","a")
    s.append(op)

    let arr=["veg chef","non-veg","multi-task"]
    console.log(arr)
    let arr1=arr.sort()
    console.log(arr1)
    for(i=0;i<=arr1.length-1;i++)
    {
        let p1=document.createElement("option")
        console.log(p1)
        // p1.innerHTML=arr1[i]
        let c=document.createTextNode(arr1[i]);
        console.log(c)
        p1.append(c)
        s.append(p1)
    }



            let s1=document.createElement("select");
            let op2=document.createElement("option")
            op2.innerHTML="SHOWS"
            s1.append(op2)

            let arr2=["masterchef","Abhiruchi","Babaihotel"]
            console.log(arr)
            let arr3=arr2.sort()
            console.log(arr3)


            for(i=0;i<=arr3.length-1;i++)
            {
                let p2=document.createElement("option")
                console.log(p2)
                // p1.innerHTML=arr1[i]
                let c1=document.createTextNode(arr3[i]);
                console.log(c1)
                p2.append(c1)
                s1.append(p2)
            }




            let s2=document.createElement("select");
            let op3=document.createElement("option")
            op3.innerHTML="RECEPIES"
            s2.append(op3)

            let arr4=["CHICKEN","MUTTON","FISH"]
            console.log(arr4)
            let arr5=arr4.sort()
            console.log(arr5)


            for(i=0;i<=arr5.length-1;i++)
            {
                let p3=document.createElement("option")
                console.log(p3)
                // p1.innerHTML=arr1[i]
                let c2=document.createTextNode(arr3[i]);
                console.log(c2)
                p3.append(c2)
                s2.append(p3)
            }



            // let s3=document.createElement("select");
            // let op4=document.createElement("option")
            // op3.innerHTML="RECEPIES"
            // s3.append(op4)
            // let arr6=["CHICKEN","MUTTON","FISH"]
            // console.log(arr6)
            // let arr7=arr6.sort()
            // console.log(arr7)


            // for(i=0;i<=arr6.length-1;i++)
            // {
            //     let p4=document.createElement("option")
            //     console.log(p4)
            //     // p1.innerHTML=arr1[i]
            //     let c3=document.createTextNode(arr6[i]);
            //     console.log(c3)
            //     p4.append(c3)
            //     s3.append(p4)
            // }

            




let t=document.createElement("table")
t.innerHTML="BLOG"
t.setAttribute("id","c")







let body=document.body;
body.append(d)
d.append(img1)
body.append(d1)
d1.append(p)
d1.append(s)
d1.append(s1)
d1.append(s2)
d1.append(t)




