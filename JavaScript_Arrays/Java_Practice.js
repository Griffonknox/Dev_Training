
function AddNumb(p1, p2) {
    return p1 + p2;
}


var test = AddNumb(4, 6);
console.log(test);


var arr = [1,2,3,4,5,6];

for (var i = 0; i < arr.length; i ++) {
    if (arr[i] % 2 == 0) {
        console.log(arr[i])
    }
}