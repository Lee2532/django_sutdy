function funcName() { console.log('arg') };

function test(a,b) {
    console.log('홀뤼쉣')
    c = arrow_function_test(a,b)
    console.log(c)
};

// fucntion name            iunput  return
let arrow_function_test  = (a, b) => a+b;
/*
// same function
let arrow_function_test = function(a, b) {
    return a+b
}
*/

