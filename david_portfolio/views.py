from django.shortcuts import render


def custom_404(req,exception):
    return render( req, "custom.html", status=404)
