// SM4 Web UI controller

document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('upload-form');
    const decryptForm = document.getElementById('decrypt-form');
    const fileList = document.getElementById('file-list');

    if (uploadForm) {
        uploadForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            try {
                const resp = await fetch('/upload', { method: 'POST', body: formData });
                const data = await resp.json();
                alert(data.message);
                if (resp.ok) loadFileList();
            } catch (err) {
                alert('Upload failed: ' + err.message);
            }
        });
    }

    if (decryptForm) {
        decryptForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            try {
                const resp = await fetch('/decrypt', { method: 'POST', body: formData });
                const data = await resp.json();
                alert(data.message);
            } catch (err) {
                alert('Decrypt failed: ' + err.message);
            }
        });
    }

    if (fileList) {
        loadFileList();
    }

    async function loadFileList() {
        try {
            const resp = await fetch('/files');
            const data = await resp.json();
            fileList.innerHTML = '';
            if (data.files && data.files.length > 0) {
                data.files.forEach(f => {
                    const li = document.createElement('li');
                    li.textContent = f;
                    fileList.appendChild(li);
                });
            } else {
                fileList.innerHTML = '<li>No files uploaded</li>';
            }
        } catch (err) {
            console.error('Failed to load file list:', err);
        }
    }
});
