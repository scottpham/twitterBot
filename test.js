    var dataObject = [{'date': 'May 5', 'place': 'San Francisco', 'magnitude': '4.5'}, {'date': 'Jan 1', 'place': 'Taipei', 'magnitude': '6'}]
    var columns = ['date', 'magnitude', 'place'];
    var textInserts = ['An earthquake occurred on the date of ', ', at a magnitude of ', ', and in the location of '];
  
    function tweet(dataObject, columns, textInserts) {
    console.log(dataObject);
    console.log(columns);
    console.log(textInserts);
    $.ajax({
    url: "/",
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify({"data":dataObject, "columns":columns, "text_inserts":textInserts})
    }).done(function(){
      alert("Bot creation completed");
    });
  }

  $("#ajax").click(function() {
    tweet(dataObject, columns, textInserts);
  });

