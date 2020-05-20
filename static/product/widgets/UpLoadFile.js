function change_image(tag){
    console.log('tag',tag)
    var preview = document.getElementById(tag.name+'-image');
    var eleFile = document.getElementById(tag.name+'-input');
    console.log('preview',preview)
    console.log('eleFile',eleFile)
    var file = tag.files[0];                
    // 确认选择的文件是图片                
    if(file.type.indexOf("image") == 0) {
        var reader = new FileReader();
        reader.readAsDataURL(file);                    
        reader.onload = function(e) {
            // 图片base64化
            var newUrl = this.result;
            console.log('preview',preview.src)
            preview.src = newUrl;
        };
    }
}