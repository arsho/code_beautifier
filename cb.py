import os, html

def get_file_list(folder_path):
    final_list = []
    file_list = os.listdir(folder_path)
    for single_file in file_list:
        file_path = os.path.join(folder_path, single_file)
        if os.path.isfile(file_path):
            final_list.append(file_path)
    return final_list

def get_file_content(single_file_path, escape_html):
    file_content_str = ''
    current_file = open(single_file_path,"r")
    file_content_list = current_file.readlines()
    file_content_str = "".join(file_content_list)
    if escape_html == True:
        file_content_str=html.escape(file_content_str)
    current_file.close()
    return file_content_str

try:
    print("================================================================")
    print("                     Code Beautifier")
    print("================================================================")    
    print("Keep your codes in \"code\" folder in the same path of cb.py\n")
    output_filename=input("Enter ouput filename in a word(without extension): ")
    header_text = """<!DOCTYPE html>
<html>

<head>

    <meta charset="UTF-8">
    <meta name="description" content="Code Beautifier by arsho">
    <meta name="keywords" content="Code Beautifier, arsho, cb, highlight">
    <meta name="author" content="Ahmedur Rahman Shovon">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" href="https://upload.wikimedia.org/wikipedia/commons/7/71/Page_code.png" type="image/x-icon">
    
    <title>Code Beautifier</title>

    <!-- Core CSS - Include with every page -->
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

    <!-- Optional theme -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.6.3/css/font-awesome.min.css" rel="stylesheet">


	<!-- Highlight -->
	<link rel="stylesheet" title="androidstudio" href="http://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.5.0/styles/androidstudio.min.css">
	<link rel="stylesheet" title="default" href="http://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.5.0/styles/default.min.css">
	<link rel="stylesheet" title="dracula" href="http://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.5.0/styles/dracula.min.css">
	<link rel="stylesheet" title="github" href="http://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.5.0/styles/github.min.css">
	<link rel="stylesheet" title="foundation" href="http://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.5.0/styles/foundation.min.css">
	<link rel="stylesheet" title="idea" href="http://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.5.0/styles/idea.min.css">
	<link rel="stylesheet" title="tomorrow" href="http://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.5.0/styles/tomorrow.min.css">
	<link rel="stylesheet" title="googlecode" href="http://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.5.0/styles/googlecode.min.css">
	<link rel="stylesheet" title="github-gist" href="http://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.5.0/styles/github-gist.min.css">
	<link rel="stylesheet" title="solarized-light" href="http://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.5.0/styles/solarized-light.min.css">

	<script src="http://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.5.0/highlight.min.js"></script>
	<script>hljs.initHighlightingOnLoad();</script>
        <link href="https://fonts.googleapis.com/css?family=Ubuntu" rel="stylesheet">	
	<style>
        body {
          padding-top: 70px;
          font-family: 'Ubuntu', sans-serif !important;
          background: #e8e8e8;
          min-height: 1000px;
        }
        .main{
	  background: rgba(255, 255, 255, 0.85);
	  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.5);	  
        }
        .panel-default .panel-heading:hover
        {
          cursor: pointer;
          color: #333;
          background: #ccc;
        }        
	</style>
</head>

<body>

    <!-- Fixed navbar -->
    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="">Code Beautifier</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <ul class="nav navbar-nav navbar-right">
            <li class="dropdown">
              <a href="" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false"><i class="fa fa-user fa-fw"></i> <span class="caret"></span></a>
              <ul class="dropdown-menu">
                <li><a href="http://github.com/arsho"><i class="fa fa-github fa-fw"></i> Created By Shovon</a></li>
                <li><a href="https://www.facebook.com/ars.shovon"><i class="fa fa-facebook fa-fw"></i> Connect In Facebook</a></li>
              </ul>
            </li>        
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>
    <div id="wrapper">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="panel panel-primary main">
                        <div class="panel-heading">
                            <div class="btn-group pull-right">
			    	<select id="theme_select" class="form-control input-sm">
					<option value="default">Default</option>				
					<option value="github">Github</option>				
					<option value="github-gist">Github Gist</option>				
					<option selected="selected" value="androidstudio">Android Studio</option>				
					<option value="googlecode">Google Code</option>				
					<option value="idea">Idea</option>				
					<option value="dracula">Dracula</option>				
					<option value="tomorrow">Tomorrow</option>				
					<option value="foundation">Foundation</option>				
					<option value="solarized-light">solarized-light</option>				
				</select>
			    </div>
			    <h3 class="panel-title" style="padding-top: 7.5px;">
                            Beautified Code <small>(Click on the title to toggle collapse mode)</small>
                            </h3>
			    <div class="clearfix"></div>
                        </div>
                        <!-- .panel-heading -->
                        <div class="panel-body">
                            <div class="panel-group" id="accordion">

"""
    footer_text = """                    </div>
                    <!-- /.accordian -->
                    </div>
                    <!-- /.panelbody -->
                    </div>
                    <!-- /.panel -->
                </div>
                <!-- /.col-lg-12 -->
            </div>
            <!-- /.row -->
        </div>
        <!-- /#page-wrapper -->

    </div>
    <!-- /#wrapper -->

    <!-- Core Scripts - Include with every page -->
    <script src="https://code.jquery.com/jquery-2.2.4.min.js" integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44=" crossorigin="anonymous"></script>
    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>


    <!-- Page-Level Plugin Scripts - Panels and Wells -->

    <script>
    // tooltip demo
    $('#accordion').tooltip({
        selector: "[data-toggle=tooltip]",
        container: "body"
    })

    // popover demo
    $("[data-toggle=popover]")
        .popover()
    function selectStyle(e)
    {
	$("link[title]").each(function(t,i)
		{i.disabled=i.title!=e}
	)
    }
    $("#theme_select").on("change",function(){
	$current_val = $(this).val();
	console.log($current_val);
	selectStyle($current_val);
    })

    </script>

</body>

</html>
"""

    output_str = ''
    output_str += header_text
    file_list = get_file_list("code")
    file_cnt = 0
    new_line = "\n"
    for single_file in file_list:
        if single_file[-1] == "~":
            continue
        single_filename = single_file.split("/")[1]
        div_id="div_"+str(file_cnt);
        file_content = get_file_content(single_file, True)
        output_str += "<!-- .panel panel-default starts -->"+new_line
        output_str += "<div data-toggle=\"tooltip\" data-placement=\"top\" title=\"Click to toggle "+single_filename+"\" class=\"panel panel-default\">"+new_line
        output_str += "<!-- .panel-heading -->"+new_line
        output_str += "<div data-toggle=\"collapse\" href=\"#"+div_id+"\" class=\"panel-heading\">"+new_line
        output_str += "<h3 class=\"panel-title\">"+single_filename+"</h3>"+new_line
        output_str += "</div>"+new_line
        output_str += "<!-- ./panel-heading -->"
        output_str += "<!-- .panel-collapse collapse -->"+new_line
        output_str += "<div id=\""+div_id+"\" class=\"panel-collapse collapse\">"+new_line
        output_str += "<!-- .panel-body -->"+new_line
        output_str += "<div class=\"panel-body\">"+new_line
        output_str += "<pre><code>"+new_line
        output_str += file_content+new_line
        output_str += "</code></pre>"+new_line
        output_str += "</div>"+new_line
        output_str += "<!-- ./panel-body -->"+new_line
        output_str += "</div>"+new_line
        output_str += "<!-- ./panel-collapse collapse -->"+new_line
        output_str += "</div>"+new_line
        output_str += "<!-- ./panel panel-default ends -->"+new_line

        file_cnt += 1
        
    output_str += footer_text
    output_filename_html = output_filename+".html"
    output = open(output_filename_html,"w")
    output.writelines(output_str)
    output.close()

    print("")
    print("Code Beautifier has created "+output_filename_html)
    print("================================================================")
    print(str(file_cnt)+" beautified code are added in "+output_filename_html+".")
    print("Note that "+output_filename_html+" is a standalone file.\nSo it can be shared easily.")
    print("")
    print("================================================================")
    print("             * Thanks for using Code Beautifier *")
    print("================================================================")
except Exception as e:
    print(str(e))
