$(document).ready(function(){
    setInterval(function(){
        let s_class = $("#class :selected").text();
        let sort =  $("#sort :selected").text();
        let date = document.getElementById("date").value;

        if (s_class == "Select Class") {
            s_class = "all";
        }
        if (sort == "Sort By") {
            sort = "none";
        }
        if (date == "") {
            date = "none";
        }
        
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:8000/api/list",
            data: {"sort": sort, "class": s_class, "date": date},
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
                                    <td>${entry.Status}</td>
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