function sendPost(url, data) {
  // 创建一个新的XMLHttpRequest对象
  var xhr = new XMLHttpRequest();
  var res = '';

  // 配置POST请求
  xhr.open('POST', url, false);
  xhr.setRequestHeader('Content-Type', 'application/json');

  // 设置请求完成的回调函数
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      res = xhr.responseText
    }
  };

  // 发送请求
  //xhr.send(JSON.stringify(data));
  xhr.send(data);
  return res;
}
