;(function(win) {
    win.CreateOnGithubPlugin = {}
  
    function create(docBase, docEditBase, title) {
      title = title || 'Edit on github'
      docEditBase = docEditBase || docBase.replace(/\/blob\//, '/edit/')
  
      function editDoc(event, vm) {
        var docName = vm.route.file
        docName = docName.replace('smeup-wiki/','')
        console.log(docName)
  
        if (docName) {
          var editLink = docEditBase + docName
          window.open(editLink)
          event.preventDefault()
          return false
        } else {
          return true
        }
      }
  
      win.CreateOnGithubPlugin.editDoc = editDoc
  
      return function(hook, vm) {
        win.CreateOnGithubPlugin.onClick = function(event) {
          CreateOnGithubPlugin.editDoc(event, vm)
        }
  
        var header = [
          '<div style="overflow: auto">',
          '<p style="float: right"><a href="',
          docBase,
          '" target="_blank" onclick="CreateOnGithubPlugin.onClick(event)">',
          title,
          '</a>&nbsp;&nbsp;&nbsp;&nbsp;</p>',
          '</div>'
        ].join('')
  
        hook.afterEach(function (html) {
          return header + html
        })
      }
    }
  
    win.CreateOnGithubPlugin.create = create
  }) (window)