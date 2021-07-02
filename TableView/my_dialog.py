
# ----------------------------------------
# Created: 2021/06/30
# Desc: a editable list_dialog
# ----------------------------------------

import ui


class list_dialog_class(object):

    def __init__(self, title, items):
        if items==None: items=[]
        self.selected_item = None
        self.edited_list = None
        
        self.table = ui.TableView()
        ds = ui.ListDataSource(items)
        ds.move_enabled = True
        ds.delete_enabled = False
        self.ds = ds

        self.table.data_source = ds
        self.table.name = title
        self.table.width= 500
        
        ds.action = self.row_selected
        self.table.delegate = ds
        

        rb = ui.ButtonItem()
        self.rb = rb
        rb.title = 'Edit'
        rb.action = self.edit_button_tapped
        self.table.right_button_items =[rb]
        
        
    def edit_button_tapped(self, sender):
        def Animation():
            self.table.alpha = .8 if self.table.alpha == 1.0 else 1.0
            
            global edited_list
            if self.rb.title == 'Done':
                self.edited_list = self.ds.items

            self.rb.title = 'Done' if self.rb.title == 'Edit' else 'Edit'
            self.rb.action = self.edit_button_tapped
            self.table.right_button_items =[self.rb]
            
            self.ds.delete_enabled = not self.ds.delete_enabled
            self.table.editing = not self.table.editing
            
        ui.animate(Animation, duration=0.3)
    
    def row_selected(self, ds):
        self.selected_item = ds.items[ds.selected_row]
        self.table.close()



def list_dialog(title='', items=None):
    c = list_dialog_class(title, items)
    c.table.present('sheet')
    c.table.wait_modal()
    return c.selected_item, c.edited_list



# ----------------------------------------
if __name__ == '__main__':
    y = list_dialog(title='test', items=['test1','test2','test3'])
    print(y)
    
    # if y[0] != None: print('string')
    # if y[1] != None: print('list')
    

