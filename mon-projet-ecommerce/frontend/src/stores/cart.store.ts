import { create } from 'zustand';
import { persist } from 'zustand/middleware';

interface CartItem {
  id: string;
  product_id: number;
  name: string;
  price: number;
  quantity: number;
  image: string;
  variant?: string;
  max_stock: number;
}

interface CartStore {
  items: CartItem[];
  addItem: (item: Omit<CartItem, 'id'>) => void;
  removeItem: (id: string) => void;
  updateQuantity: (id: string, quantity: number) => void;
  clearCart: () => void;
  totalItems: () => number;
  totalPrice: () => number;
}

export const useCartStore = create<CartStore>()(
  persist(
    (set, get) => ({
      items: [],
      
      addItem: (newItem) => {
        set((state) => {
          const existing = state.items.find(
            (item) => item.product_id === newItem.product_id && item.variant === newItem.variant
          );
          
          if (existing) {
            const maxQuantity = existing.max_stock;
            const newQuantity = Math.min(existing.quantity + newItem.quantity, maxQuantity);
            return {
              items: state.items.map((item) =>
                item.id === existing.id
                  ? { ...item, quantity: newQuantity }
                  : item
              ),
            };
          }
          
          return {
            items: [...state.items, { ...newItem, id: crypto.randomUUID() }],
          };
        });
      },
      
      removeItem: (id) => {
        set((state) => ({
          items: state.items.filter((item) => item.id !== id),
        }));
      },
      
      updateQuantity: (id, quantity) => {
        set((state) => ({
          items: state.items.map((item) =>
            item.id === id
              ? { ...item, quantity: Math.min(quantity, item.max_stock) }
              : item
          ),
        }));
      },
      
      clearCart: () => set({ items: [] }),
      
      totalItems: () => {
        return get().items.reduce((acc, item) => acc + item.quantity, 0);
      },
      
      totalPrice: () => {
        return get().items.reduce((acc, item) => acc + item.price * item.quantity, 0);
      },
    }),
    {
      name: 'cart-storage', //Nom du localStorage
    },
  )
);