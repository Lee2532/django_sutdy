

let get_api_key = () => {
    let reader = new FileReader();
    reader.onload = function () {
    textContents.innerText = reader.result;
    };
    reader.readAsText("../../api_key/key.txt", "UTF-8");
    console.log(reader)
}



