import { Component, OnInit } from '@angular/core';

import { CommonService } from '../common.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  constructor(
    private commonService:CommonService,
  ) { }

  ngOnInit(): void {
  }

  buttonClick(){
    this.commonService.func01();
  }

}
