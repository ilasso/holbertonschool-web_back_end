const Utils = {
    calculateNumber (type, a, b) {
        switch (type) {
            case 'SUM':
                return Math.round(a) + Math.round(b);        
                break;
            case 'SUBTRACT':
                    return Math.round(a) - Math.round(b);
                    break;
            case 'DIVIDE':
                if (!Math.round(b)) return 'Error';
                return Math.round(a) / Math.round(b);
                break;                
            default:
                break;
        }
    
    }
}
module.exports = Utils;