<script>
	//removes curly braces from array
	twitterBot.fixArray = function(myArray) {
		var fixedArray = [];
		$.each(myArray, function (index, value){
			len = value.length;
			var x = myArray[index].replace(value, value.slice(2,len-2));
			fixedArray.push(x);
			} )
		console.log("fixed array = " + fixedArray);
		return fixedArray;	
	}
	
	//generates preview tweet
	twitterBot.tweetPreview = function() {
		var tweetPreviewString = document.forms.form2.tweet.value;
		this.tweetPreviewString = tweetPreviewString;
		console.log("preview string = " + tweetPreviewString);
		var myRe = /{{(.*?)}}/g;
		myArray = tweetPreviewString.match(myRe);
		this.fixedArray = this.fixArray(myArray);
		$.each(this.fixedArray, function(index, value) {
			tweetPreviewString = tweetPreviewString.replace("{{" + value + "}}", testData[1][value]);
		})
		$("#tweetPreview").html(tweetPreviewString);
	};

	//generates clean lists for python
	twitterBot.sendToPython = function (){ 
		x = this.fixedArray; //clean array of dict keys, send this to python it's good
		var myRe = /{{(.*?)}}/g;
		var cleanTweetString = this.tweetPreviewString.split(myRe);
		this.cleanTweetArray = $(cleanTweetString).not(this.fixedArray).get();
		this.cleanTweetArray = jQuery.grep(this.cleanTweetArray, function(n, i){
			return (n !== "" && n != null && n != " ");
		})
	};
//		object = {}
//		object[counter]=
//			counter++
</script>