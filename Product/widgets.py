from django import forms

class UpLoadFile(forms.ClearableFileInput):
    template_name = 'widgets/UpLoadFile.html'
    class Media:
        # css = {
        #      'all': ('/css/pretty.css',),
        # }
        js = ["product/widgets/UpLoadFile.js"] #不知道为什么只能用[],和官方教程用()不一样