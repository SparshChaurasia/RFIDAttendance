$(document).ready(function(){
    setInterval(function(){
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:8000/api/list",
            success: function(response){
                $("#table-data-container").empty()
                var i = 1;
                for (var key in response) {
                    var entry = response[key];
                    var html = `<tr>
                                    <th scope="row">${i}</th>
                                    <td>${entry.StudName}</td>
                                    <td>${entry.StudClass}</td>
                                    <td>${entry.Time}</td>
                                    <td>-</td>
                                </tr>`;
                    $("#table-data-container").append(html);

                    i++;
                }
            },
            error: function(response){
                alert("An error occured")
            }
        });
    }, 1500);
});