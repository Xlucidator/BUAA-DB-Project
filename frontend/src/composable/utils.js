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