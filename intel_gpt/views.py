from django.shortcuts import render
from documents.models import Document
from documents.forms import DocumentForm

def home(request):
    documents = Document.objects.all()
    form = DocumentForm()
    message = None

    if request.method == 'POST':
        if request.FILES:
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                newdoc = Document(document=request.FILES['document'])
                newdoc.save()
        else:
            message = request.POST.get('name')

    # Read file contents if a document is uploaded
    file_contents = None
    if documents:
        with documents.last().document.open() as f:
            file_contents = f.read()

    return render(request, 'home.html', {'documents': documents, 'form': form, 'message': message, 'file_contents': file_contents})
