let img1=document.createElement("img")
img1.src="nature.png"
img1.setAttribute("id","img1")

let btn1=document.createElement("button")
btn1.innerHTML=">"
btn1.setAttribute("id","btn1")
let btn2=document.createElement("button")
btn2.innerHTML="<"
btn2.setAttribute("id","btn2")

let arr=["butter1.jpg","butter.jpg","butter2.jpg","butter3.jpg","butter4.jpg","butter5.jpg","butter6.jpg","butter7.jpg"]
//  ------------------first way code process---------------

// ----------------forward code-------------------
let i=0;
btn1.addEventListener("click",
function()
{
    img1.src=arr[i];
    i++;
    if(i==arr.length)
    {
        i=0;
    }
}
)

// -------------backward code-----------

let j=arr.length-1;
btn2.addEventListener("click",
function()
{
    img1.src=arr[j];
    j--;
    if(j<0)
    {
        j=arr.length-1;
    }
}
)

let b=document.body
b.append(img1)
b.append(btn1,btn2)