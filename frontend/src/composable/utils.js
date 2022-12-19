import {ElNotification} from "element-plus";

export function NOTATION(success, msg){
    if(success) {
        return ElNotification({
            title: 'Success',
            message: msg,
            type: 'success',
        })
    } else {
        return ElNotification({
          title: 'Error',
          message: msg,
          type: 'error',
        })
    }
}

export function gotoBottom() {
    const box = document.getElementsByClassName('message-panel-box')[0]
    this.$nextTick(() => {
        box.scrollTop = box.scrollHeight
    })
}