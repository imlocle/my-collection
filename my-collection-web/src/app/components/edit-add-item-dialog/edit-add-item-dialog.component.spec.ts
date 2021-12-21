import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditAddItemDialogComponent } from './edit-add-item-dialog.component';

describe('EditAddItemDialogComponent', () => {
  let component: EditAddItemDialogComponent;
  let fixture: ComponentFixture<EditAddItemDialogComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EditAddItemDialogComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EditAddItemDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
