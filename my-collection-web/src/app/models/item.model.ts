import { State, City } from './state.model';

// Snake case to match schema of API
export class Item {
  constructor(
    public name: string,
    public purchased_price: number,
    public category: string,
    public artist?: string,
    public manufacturer?: string,
    public model_number?: string,
    public state?: State,
    public sku?: string,
    public city?: City,
    public description?: string,
    public _id?: number,
    public updatedOn?: Date,
    public createdOn?: Date,
    public lastUpdatedBy?: string
  ) {}
}
