var HOME_URL = "/";

function delete_node(noteId) {
  console.log(noteId);
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = HOME_URL;
  });
}
